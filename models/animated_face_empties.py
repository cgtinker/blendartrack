from utils.custom_data.iCustomData import ImportModel
from utils.json import decoder
from utils.blend import name, collection, keyframe, scene, objects, reference


class AnimatedFaceEmpties(ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.batch = batch
        self.title = title

        self.parent_name = "Face_Motion_"
        self.collection = "Face"
        self.model = None

        self.parent = None
        self.empties = None

    def initialize(self):
        # set frame and vertex location data as mesh model
        for data in self.json_data[self.title]:
            mesh_vertices = [decoder.get_vert_data(data['pos'][i]) for i in range(len(data['pos']))]
            frame = data['frame']
            tmp = FaceMesh(mesh_vertices, frame)
            self.model.append(tmp)

        self.model = set(self.model)

    # check for user input before
    def generate(self):
        if self.batch:
            self.parent = name.get_object_by_name(name=self.parent_name)
        else:
            self.parent = reference.generate_empty_at(
                px=0, py=0, pz=0, size=1, name=self.parent_name)

        self.empties = reference.generate_empties((len(self.model[0].vertices)), size=0.0025)

    def animate(self):
        active_scene = scene.set_scene_frame_end(self.model)
        # key framing empties
        for data in self.model:
            # data.init_frame(active_scene)
            keyframe.init_keyframe(data.frame, active_scene)
            for i in range(len(data.vertices)):
                if data.vertices:
                    pos = data.vertices[i].get_pos()
                    keyframe.set_pos_keyframe(
                        pos[0], pos[1], pos[2], self.empties[i])

    def structure(self):
        for obj in self.empties:
            obj.parent = self.parent

        collection.add_list_to_collection(self.empties, self.collection)
        scene.disable_relation_lines()


class FaceMesh:
    def __init__(self, mesh_vertices, frame):
        self.vertices = mesh_vertices
        self.frame = frame

    def get_positions(self):
        vertices = []
        for i in range(len(self.vertices)):
            if self.vertices:
                vertices.append(self.vertices[i].get_pos())
        return vertices

    def print_contents(self):
        print("frame:", self.frame)
        for mesh_vertex in self.vertices:
            mesh_vertex.print_vert_content()


class MeshVertex:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def get_pos(self):
        return [self.px, self.py, self.pz]

    def print_vert_content(self):
        print('vert: px', self.px, 'vert: py', self.py, 'vert: pz', self.pz)



