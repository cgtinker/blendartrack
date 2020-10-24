# from typing import List
from typing import List

from main import jsonDecoder as jd
from main import keyframeAssistent as ka


class PoseData:
    def __init__(self, px, py, pz, rx, ry, rz, frame):
        # assign pos
        self.px = px
        self.py = py
        self.pz = pz
        # assign rotation_euler
        self.rx = rx
        self.ry = ry
        self.rz = rz
        # assign frame
        self.frame = frame

    def init_frame(self, scene, obj):
        ka.InitKeyframe(self.frame, scene, obj)

    def key_pos(self, obj):
        ka.PosKeyframes(self.px, self.py, self.pz, obj)

    def key_rot(self, obj):
        ka.RotKeyframes(self.rx, self.ry, self.rz, obj)

    def print_content(self):
        print('px', self.px, 'py', self.py, 'pz', self.pz, 'rx', self.rx, 'ry', self.ry, 'rz', self.rz, 'f', self.frame)


def init_pose_list(json_data):
    # store pose data
    global POSE_LIST
    POSE_LIST = []
    # decoding json
    for data in json_data['poseList']:
        px, py, pz = jd.SplitPosData(data)
        rx, ry, rz = jd.SplitRotData(data)
        frame = (data['frame'])
        # append data to list
        obj = PoseData(px, py, pz, rx, ry, rz, frame)
        POSE_LIST.append(obj)
