from main.common import keyframeAssistent as kA, jsonDecoder as jD


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
        kA.init_keyframe(self.frame, scene, obj)

    def key_pos(self, obj):
        kA.pos_keyframes(self.px, self.py, self.pz, obj)

    def key_rot(self, obj):
        kA.rot_keyframes(self.rx, self.ry, self.rz, obj)

    def print_content(self):
        print('px', self.px, 'py', self.py, 'pz', self.pz, 'rx', self.rx, 'ry', self.ry, 'rz', self.rz, 'f', self.frame)


def init_pose_list(json_data):
    # store pose data
    global CUR_DATA
    CUR_DATA = []
    # decoding json
    for data in json_data['poseList']:
        px, py, pz = jD.split_pos_data(data)
        rx, ry, rz = jD.split_rot_data(data)
        frame = (data['frame'])
        # append data to list
        obj = PoseData(px, py, pz, rx, ry, rz, frame)
        CUR_DATA.append(obj)
    return CUR_DATA
