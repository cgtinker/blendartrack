from module.execution.processing.objects import KeyframeAssistent
from module.preperation.importing import DecodeJson
import importlib
importlib.reload(KeyframeAssistent)
importlib.reload(DecodeJson)


class PoseData:
    def __init__(self, px, py, pz, rx, ry, rz, frame):
        self.px = px
        self.py = pz
        self.pz = py
        self.rx = -rx   # TODO: still requires x mirroring
        self.ry = rz
        self.rz = -ry
        self.frame = frame

    def init_frame(self, scene):
        KeyframeAssistent.init_keyframe(self.frame, scene)
        print("retargeting camera pose data at frame ", self.frame, end='\r')

    def key_pos(self, obj):
        KeyframeAssistent.set_pos_keyframe(self.px, self.py, self.pz, obj)

    def key_rot(self, obj, x_offset):
        KeyframeAssistent.set_rot_keyframe(self.rx + x_offset, self.ry, self.rz, obj)

    def print_contents(self):
        print("pose data:", 'px', self.px, 'py', self.py, 'pz', self.pz, 'rx', self.rx, 'ry', self.ry, 'rz', self.rz, 'f', self.frame)


def init_pose_model(json_data, title):
    # array to store pose data
    pose_model = []
    # decoding json
    for data in json_data[title]:
        px, py, pz = DecodeJson.get_pos_data(data)
        rx, ry, rz = DecodeJson.get_rot_data(data)
        frame = (data['frame'])
        # append data to list
        tmp = PoseData(px, py, pz, rx, ry, rz, frame)
        pose_model.append(tmp)
    return pose_model
