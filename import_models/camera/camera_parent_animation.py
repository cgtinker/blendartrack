from ...utils.blend import keyframe, scene, reference, collection, constraints
from ...utils.json import decoder
from .. import pose, iCustomData
from ...utils import reference_names


class CameraParent(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.batch = batch
        self.title = title

        self.model = []
        self.parent = None

        self.camera_name = reference_names.ar_camera
        self.camera = None
        self.name = reference_names.camera_parent
        self.collection = reference_names.cam_col

    def initialize(self):
        for data in self.json_data[self.title]:
            px, py, pz = decoder.get_pos_data(data)
            rx, ry, rz = decoder.get_rot_data(data)
            frame = (data['frame'])
            tmp = pose.PoseData(px, py, pz, rx, ry, rz, frame)
            self.model.append(tmp)

        self.model = set(self.model)

    def generate(self):
        if self.batch:
            self.camera = reference.create_new_camera(self.camera_name)
            self.parent = reference.generate_empty_at(
                px=0, py=0, pz=0, name=self.name, size=1)
        else:
            if reference.is_object_selected():
                self.parent = reference.get_selected_object()
            else:
                self.parent = reference.generate_empty_at(
                    px=0, py=0, pz=0, name=self.name, size=1)

    def animate(self):
        active_scene = scene.set_scene_frame_end(self.model)
        for data in self.model:
            keyframe.init_keyframe(data.frame, active_scene)
            keyframe.set_pos_keyframe(data.px, data.py, data.pz, self.parent)
            keyframe.set_rot_keyframe(data.rx + 90, data.ry, data.rz, self.parent)

    def structure(self):
        constraints.add_copy_location_constraint(obj=self.camera, target_obj=self.parent, use_offset=False)
        constraints.add_copy_rotation_constraint(obj=self.camera, target_obj=self.parent, invert_y=True)
        collection.add_obj_to_collection(self.collection, self.camera)
        collection.add_obj_to_collection(self.collection, self.parent)
