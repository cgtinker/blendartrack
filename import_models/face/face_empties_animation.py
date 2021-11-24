from import_models.iCustomData import ImportModel
from utils.blend import name, collection, keyframe, scene, reference
from import_models.face import face_anim_data
import importlib
import bpy
importlib.reload(scene)


class AnimatedFaceEmpties(ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.batch = batch
        self.title = title

        self.parent_name = "Face_Motion_"
        self.collection = "Face"

        self.model = []
        self.parent = None
        self.empties = None

    def initialize(self):
        print("initialzed face empty amin")
        self.model = face_anim_data.initialize(self.json_data, self.title)

    # check for user input before
    def generate(self):
        print("generating face anim empty stuff")
        if self.batch:
            self.parent = name.get_object_by_name(name=self.parent_name)
        else:
            self.parent = reference.generate_empty_at(
                px=0, py=0, pz=0, size=1, name=self.parent_name)

        self.empties = reference.generate_empties((len(self.model[0].vertices)), size=0.0025)

    def old_animate(self):
        active_scene = scene.set_scene_frame_end(self.model)
        # key framing empties
        for data in self.model:
            # data.init_frame(active_scene)
            keyframe.init_keyframe(data.frame, active_scene)
            for i in range(len(data.vertices)):
                if data.vertices:
                    pos = data.vertices[i].get_pos()
                    keyframe.set_pos_keyframe(pos[0], pos[1], pos[2], self.empties[i])
    
    def animate(self):
        scene.set_scene_frame_end(self.model)
        frames = [x.frame for x in self.model]
        vertex_pos_data = []

        # todo -> list comprehension
        # for every vertex
        for index, _ in enumerate(self.model[0].vertices):
            vertex_px = []
            vertex_py = []
            vertex_pz = []
            # for all data in model
            for data in self.model:
                pos = data.vertices[index].get_pos()
                vertex_px.append(pos[0])
                vertex_py.append(pos[1])
                vertex_pz.append(pos[2])
            vertex_pos_data.append([vertex_px, vertex_py, vertex_pz])

        # set pos for each empty
        for i, empty in enumerate(self.empties):
            # create animation data
            empty.animation_data_create()
            empty.animation_data.action = bpy.data.actions.new(name=f"{empty.name}")

            # iter for x, y, z
            for e in range(3):
                # populate fcurves
                fc = empty.animation_data.action.fcurves.new(
                    data_path="location", index=e
                )
                fc.keyframe_points.add(count=len(frames))
                # set animation data
                fc.keyframe_points.foreach_set("co",
                                               [x for co in zip(frames, vertex_pos_data[i][e]) for x in co])
                # update
                fc.update()

    def structure(self):
        for obj in self.empties:
            obj.parent = self.parent

        collection.add_list_to_collection(self.empties, self.collection)
        scene.disable_relation_lines()
