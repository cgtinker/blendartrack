import bpy

from ....utils import string_ops
from ....utils.blend import scene


def get_constraint_dict():
    """target: [current name, empty reference, constraint type, constraint strength]"""
    constrained_bones = {
        # JAW
        "jaw_master":   ["jaw", "FaceEmpty_152", 23, scene.get_user().jaw_master_influence],
        "jaw.L.001":    ["jaw.L.001", "FaceEmpty_435", 3, scene.get_user().jaw_sides_influence],
        "jaw.R.001":    ["jaw.R.001", "FaceEmpty_215", 3, scene.get_user().jaw_sides_influence],

        # CHIN
        "chin":         ["chin", "FaceEmpty_152", 3, scene.get_user().chin_master_influence],
        "chin.R":       ["chin.R", "FaceEmpty_32", 3, scene.get_user().chin_sides_influence],
        "chin.L":       ["chin.L", "FaceEmpty_262", 3, scene.get_user().chin_sides_influence],

        # LIPS
        "lips.R":       ["lips.R", "FaceEmpty_61", 3, scene.get_user().lips_influence],
        "lips.L":       ["lips.L", "FaceEmpty_291", 3, scene.get_user().lips_influence],
        "lips.T":       ["lips.T", "FaceEmpty_0", 3, scene.get_user().lips_influence],

        # NOSE
        "nose.L":       ["nose.L", "FaceEmpty_437", 3, scene.get_user().nose_influence],
        "nose.L.001":   ["nose.L.001", "FaceEmpty_358", 3, scene.get_user().nose_influence],
        "nose.R":       ["nose.R", "FaceEmpty_217", 3, scene.get_user().nose_influence],
        "nose.R.001":   ["nose.R.001", "FaceEmpty_129", 3, scene.get_user().nose_influence],

        # BROW
        "brow.T.R":     ["brow.T.R", "FaceEmpty_143", 3, scene.get_user().brow_sides_influence],
        "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70", 3, scene.get_user().brow_sides_influence],
        "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107", 3, scene.get_user().brow_master_influence],
        "brow.B.R":     ["brow.B.R", "FaceEmpty_247", 3, scene.get_user().brow_master_influence],
        "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30", 3, scene.get_user().brow_master_influence],
        "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27", 3, scene.get_user().brow_master_influence],
        "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56", 3, scene.get_user().brow_master_influence],
        "brow.B.R.004": ["brow.B.R.004", "FaceEmpty_190", 3, scene.get_user().brow_master_influence],

        "brow.T.L":     ["brow.T.L", "FaceEmpty_372", 3, scene.get_user().brow_sides_influence],
        "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300", 3, scene.get_user().brow_sides_influence],
        "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336", 3, scene.get_user().brow_master_influence],
        "brow.B.L":     ["brow.B.L", "FaceEmpty_467", 3, scene.get_user().brow_master_influence],
        "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260", 3, scene.get_user().brow_master_influence],
        "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257", 3, scene.get_user().brow_master_influence],
        "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286", 3, scene.get_user().brow_master_influence],
        "brow.B.L.004": ["brow.B.L.004", "FaceEmpty_414", 3, scene.get_user().brow_master_influence],

        # EYES
        "lid.T.R":      ["lid.T.R", "FaceEmpty_33", 3, scene.get_user().lid_influence],
        "lid.T.R.001":  ["lid.T.R.001", "FaceEmpty_161", 3, scene.get_user().lid_influence],
        "lid.T.R.002":  ["lid.T.R.002", "FaceEmpty_159", 3, scene.get_user().lid_influence],
        "lid.T.R.003":  ["lid.T.R.003", "FaceEmpty_157", 3, scene.get_user().lid_influence],
        "lid.B.R":      ["lid.B.R", "FaceEmpty_133", 3, scene.get_user().lid_influence],
        "lid.B.R.001":  ["lid.B.R.001", "FaceEmpty_154", 3, scene.get_user().lid_influence],
        "lid.B.R.002":  ["lid.B.R.002", "FaceEmpty_145", 3, scene.get_user().lid_influence],
        "lid.B.R.003":  ["lid.B.R.003", "FaceEmpty_163", 3, scene.get_user().lid_influence],

        "lid.B.L":      ["lid.B.L", "FaceEmpty_362", 3, scene.get_user().lid_influence],
        "lid.B.L.001":  ["lid.B.L.001", "FaceEmpty_381", 3, scene.get_user().lid_influence],
        "lid.B.L.002":  ["lid.B.L.002", "FaceEmpty_374", 3, scene.get_user().lid_influence],
        "lid.B.L.003":  ["lid.B.L.003", "FaceEmpty_390", 3, scene.get_user().lid_influence],
        "lid.T.L":      ["lid.T.L", "FaceEmpty_263", 3, scene.get_user().lid_influence],
        "lid.T.L.001":  ["lid.T.L.001", "FaceEmpty_388", 3, scene.get_user().lid_influence],
        "lid.T.L.002":  ["lid.T.L.002", "FaceEmpty_386", 3, scene.get_user().lid_influence],
        "lid.T.L.003":  ["lid.T.L.003", "FaceEmpty_384", 3, scene.get_user().lid_influence]}

    return constrained_bones


def get_ios_constraint_dict():
    constrained_bones = {
        'jaw_master':   ['jaw_master', 'FaceEmpty_1047', 23, scene.get_user().jaw_master_influence],
        'jaw.L.001':    ['jaw.L.001', 'FaceEmpty_1004', 3, scene.get_user().jaw_sides_influence],
        'jaw.R.001':    ['jaw.R.001', 'FaceEmpty_927', 3, scene.get_user().jaw_sides_influence],
        'chin':         ['chin', 'FaceEmpty_1047', 3, scene.get_user().chin_master_influence],
        'chin.R':       ['chin.R', 'FaceEmpty_986', 3, scene.get_user().chin_sides_influence],
        'chin.L':       ['chin.L', 'FaceEmpty_1050', 3, scene.get_user().chin_sides_influence],
        'lips.R':       ['lips.R', 'FaceEmpty_173', 3, scene.get_user().lips_influence],
        'lips.L':       ['lips.L', 'FaceEmpty_622', 3, scene.get_user().lips_influence],
        'lips.T':       ['lips.T', 'FaceEmpty_1', 3, scene.get_user().lips_influence],
        'nose.L':       ['nose.L', 'FaceEmpty_609', 3, scene.get_user().nose_influence],
        'nose.L.001':   ['nose.L.001', 'FaceEmpty_865', 3, scene.get_user().nose_influence],
        'nose.R':       ['nose.R', 'FaceEmpty_160', 3, scene.get_user().nose_influence],
        'nose.R.001':   ['nose.R.001', 'FaceEmpty_437', 3, scene.get_user().nose_influence],
        'brow.T.R':     ['brow.T.R', 'FaceEmpty_235', 3, scene.get_user().brow_sides_influence],
        'brow.T.R.001': ['brow.T.R.001', 'FaceEmpty_199', 3, scene.get_user().brow_sides_influence],
        'brow.T.R.003': ['brow.T.R.003', 'FaceEmpty_348', 3, scene.get_user().brow_master_influence],
        'brow.B.R':     ['brow.B.R', 'FaceEmpty_1156', 3, scene.get_user().brow_master_influence],
        'brow.B.R.001': ['brow.B.R.001', 'FaceEmpty_1154', 3, scene.get_user().brow_master_influence],
        'brow.B.R.002': ['brow.B.R.002', 'FaceEmpty_1152', 3, scene.get_user().brow_master_influence],
        'brow.B.R.003': ['brow.B.R.003', 'FaceEmpty_1150', 3, scene.get_user().brow_master_influence],
        'brow.T.L':     ['brow.T.L', 'FaceEmpty_670', 3, scene.get_user().brow_sides_influence],
        'brow.T.L.001': ['brow.T.L.001', 'FaceEmpty_648', 3, scene.get_user().brow_sides_influence],
        'brow.T.L.003': ['brow.T.L.003', 'FaceEmpty_781', 3, scene.get_user().brow_master_influence],
        'brow.B.L':     ['brow.B.L', 'FaceEmpty_1130', 3, scene.get_user().brow_master_influence],
        'brow.B.L.001': ['brow.B.L.001', 'FaceEmpty_1128', 3, scene.get_user().brow_master_influence],
        'brow.B.L.002': ['brow.B.L.002', 'FaceEmpty_1126', 3, scene.get_user().brow_master_influence],
        'brow.B.L.003': ['brow.B.L.003', 'FaceEmpty_1124', 3, scene.get_user().brow_master_influence],
        'lid.T.R':      ['lid.T.R', 'FaceEmpty_1181', 3, scene.get_user().lid_influence],
        'lid.T.R.001':  ['lid.T.R.001', 'FaceEmpty_1097', 3, scene.get_user().lid_influence],
        'lid.T.R.002':  ['lid.T.R.002', 'FaceEmpty_1095', 3, scene.get_user().lid_influence],
        'lid.T.R.003':  ['lid.T.R.003', 'FaceEmpty_1092', 3, scene.get_user().lid_influence],
        'lid.B.R':      ['lid.B.R', 'FaceEmpty_1089', 3, scene.get_user().lid_influence],
        'lid.B.R.001':  ['lid.B.R.001', 'FaceEmpty_1086', 3, scene.get_user().lid_influence],
        'lid.B.R.002':  ['lid.B.R.002', 'FaceEmpty_1108', 3, scene.get_user().lid_influence],
        'lid.B.R.003':  ['lid.B.R.003', 'FaceEmpty_1106', 3, scene.get_user().lid_influence],
        'lid.B.L':      ['lid.B.L', 'FaceEmpty_1081', 3, scene.get_user().lid_influence],
        'lid.B.L.001':  ['lid.B.L.001', 'FaceEmpty_1084', 3, scene.get_user().lid_influence],
        'lid.B.L.002':  ['lid.B.L.002', 'FaceEmpty_1062', 3, scene.get_user().lid_influence],
        'lid.B.L.003':  ['lid.B.L.003', 'FaceEmpty_1064', 3, scene.get_user().lid_influence],
        'lid.T.L':      ['lid.T.L', 'FaceEmpty_1180', 3, scene.get_user().lid_influence],
        'lid.T.L.001':  ['lid.T.L.001', 'FaceEmpty_1073', 3, scene.get_user().lid_influence],
        'lid.T.L.002':  ['lid.T.L.002', 'FaceEmpty_1075', 3, scene.get_user().lid_influence],
        'lid.T.L.003':  ['lid.T.L.003', 'FaceEmpty_1078', 3, scene.get_user().lid_influence],
    }
    return constrained_bones


def add_constraint(bone, data):
    constraints = {
        0:  "CAMERA_SOLVER",
        1:  "FOLLOW_TRACK",
        2:  "OBJECT_SOLVER",
        3:  "COPY_LOCATION",
        4:  "COPY_ROTATION",
        5:  "COPY_SCALE",
        6:  "COPY_TRANSFORMS",
        7:  "LIMIT_DISTANCE",
        8:  "LIMIT_LOCATION",
        9:  "LIMIT_ROTATION",
        10: "LIMIT_SCALE",
        11: "MAINTAIN_VOLUME",
        12: "TRANSFORM",
        13: "TRANSFORM_CACHE",
        14: "CLAMP_TO",
        15: "DAMPED_TRACK",
        16: "IK",
        17: "LOCKED_TRACK",
        18: "SPLINE_IK",
        19: "STRETCH_TO",
        20: "TRACK_TO",
        21: "ACTION",
        22: "ARMATURE",
        23: "CHILD_OF",
        24: "FLOOR",
        25: "FOLLOW_PATH",
        26: "PIVOT",
        27: "SHRINKWRAP"
    }

    constraint = bone.constraints.new(
        type=constraints[data[2]]
    )
    constraint.target = bpy.data.objects[data[1]]
    constraint.influence = data[3]


def update_constraint(bone, data):
    constraints = {
        0:  "CAMERA_SOLVER",
        1:  "FOLLOW_TRACK",
        2:  "OBJECT_SOLVER",
        3:  "COPY_LOCATION",
        4:  "COPY_ROTATION",
        5:  "COPY_SCALE",
        6:  "COPY_TRANSFORMS",
        7:  "LIMIT_DISTANCE",
        8:  "LIMIT_LOCATION",
        9:  "LIMIT_ROTATION",
        10: "LIMIT_SCALE",
        11: "MAINTAIN_VOLUME",
        12: "TRANSFORM",
        13: "TRANSFORM_CACHE",
        14: "CLAMP_TO",
        15: "DAMPED_TRACK",
        16: "IK",
        17: "LOCKED_TRACK",
        18: "SPLINE_IK",
        19: "STRETCH_TO",
        20: "TRACK_TO",
        21: "ACTION",
        22: "ARMATURE",
        23: "CHILD_OF",
        24: "FLOOR",
        25: "FOLLOW_PATH",
        26: "PIVOT",
        27: "SHRINKWRAP"
    }

    for constraint in bone.constraints:
        c_name = string_ops.set_lower_letter_only_string(constraint.name)
        lookup = string_ops.set_lower_letter_only_string(constraints[data[2]])

        # check constraint type
        if c_name == lookup:
            c_target_name = string_ops.set_lower_letter_only_string(constraint.target.name)
            # todo: faceempty str should be anywhere, not here..
            # check constraint target before resetting influence
            if c_target_name == "faceempty":
                constraint.influence = data[3]


def add(arm):
    is_android = is_android_device()

    bones = arm.pose.bones
    for bone in bones:
        try:
            if is_android:
                data = get_constraint_dict()[bone.name]
            else:
                data = get_ios_constraint_dict()[bone.name]
            add_constraint(bone, data)

        except KeyError:
            pass


def update(arm):
    is_android = is_android_device()
    scene.set_pose_mode()
    bones = arm.pose.bones

    for bone in bones:
        try:
            if is_android:
                data = get_constraint_dict()[bone.name]
            else:
                data = get_ios_constraint_dict()[bone.name]
            update_constraint(bone, data)

        except KeyError:
            pass

    scene.set_object_mode()


def is_android_device():
    is_android = False
    if scene.get_user().enum_device_type == "Android":
        is_android = True

    return is_android
