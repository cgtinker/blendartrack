from utils.custom_data import iCustomData
from utils.blend import name, keyframe, scene, reference, collection
from utils.json import decoder
from . import pose_data


class AnimatedFaceParentMotion(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.batch = batch
        self.title = title

        self.model = []
        self.name = "FaceParent"
        self.obj = None
        self.collection = "Face"

    def initialize(self):
        for data in self.json_data[self.title]:
            px, py, pz = decoder.get_pos_data(data)
            rx, ry, rz = decoder.get_rot_data(data)
            frame = (data['frame'])
            tmp = pose_data.PoseData(px, py, pz, rx, ry, rz, frame)
            self.model.append(tmp)

        self.model = set(self.model)

    def generate(self):
        if self.batch:
            self.obj = reference.generate_empty_at(
                px=0, py=0, pz=0, name=self.name, size=1)
        else:
            if reference.is_object_selected():
                self.obj = reference.get_selected_object()
            else:
                self.obj = reference.generate_empty_at(
                    px=0, py=0, pz=0, name=self.name, size=1)

    def animate(self):
        active_scene = scene.set_scene_frame_end(self.model)
        for data in self.model:
            keyframe.init_keyframe(data.frame, active_scene)
            keyframe.set_pos_keyframe(data.px, data.py, data.pz, self.obj)
            keyframe.set_rot_keyframe(data.rx, data.ry, data.rz, self.obj)

    def structure(self):
        collection.add_obj_to_collection(self.collection, self.obj)
