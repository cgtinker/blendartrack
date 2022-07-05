from ...utils.blend import keyframe, scene, collection, objects
from ...utils.json import decoder
from .. import iCustomData, pose
from ...utils import reference_names


class AnimatedFaceParent(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.batch = batch
        self.title = title

        self.model = []
        self.name = reference_names.face_parent
        self.obj = None
        self.collection = reference_names.face_col

    def initialize(self):
        for data in self.json_data[self.title]:
            px, py, pz = decoder.get_pos_data(data)
            rx, ry, rz = decoder.get_rot_data(data)
            frame = (data['frame'])
            tmp = pose.PoseData(px, py, pz, rx, ry, rz, frame)
            self.model.append(tmp)

    def generate(self):
        if self.batch:
            self.obj = objects.get_object_by_name(self.name)
        else:
            if objects.is_object_selected():
                self.obj = objects.get_selected_object()
            else:
                self.obj = objects.get_object_by_name(self.name)

    def animate(self):
        active_scene = scene.set_scene_frame_end(self.model)
        for data in self.model:
            keyframe.init_keyframe(data.frame, active_scene)
            keyframe.set_pos_keyframe(data.px, data.py, data.pz, self.obj)
            keyframe.set_rot_keyframe(data.rx, data.ry, data.rz, self.obj)

    def structure(self):
        collection.add_obj_to_collection(self.collection, self.obj)
