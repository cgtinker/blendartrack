import bpy

armature = bpy.data.objects["rig"]
bones = armature.pose.bones

"""target: [current name, empty reference, constraint type, constraint strength]"""
"""
constrained_bones = {
    # JAW
    "jaw_master": ["jaw_master", "FaceEmpty_152", 23,       jaw_master_influence],
    "jaw.L.001": ["jaw.L.001", "FaceEmpty_435", 3,          jaw_sides_influence],
    "jaw.R.001": ["jaw.R.001", "FaceEmpty_215", 3,          jaw_sides_influence],

    # CHIN
    "chin": ["chin", "FaceEmpty_152", 3,                    chin_master_influence],
    "chin.R": ["chin.R", "FaceEmpty_32", 3,                 chin_sides_influence],
    "chin.L": ["chin.L", "FaceEmpty_262", 3,                chin_sides_influence],

    # LIPS
    "lips.R": ["lips.R", "FaceEmpty_61", 3,                 lips_influence],
    "lips.L": ["lips.L", "FaceEmpty_291", 3,                lips_influence],
    "lips.T": ["lips.T", "FaceEmpty_0", 3,                  lips_influence],

    # NOSE
    "nose.L": ["nose.L", "FaceEmpty_437", 3,                nose_influence],
    "nose.L.001": ["nose.L.001", "FaceEmpty_358", 3,        nose_influence],
    "nose.R": ["nose.R", "FaceEmpty_217", 3,                nose_influence],
    "nose.R.001": ["nose.R.001", "FaceEmpty_129", 3,        nose_influence],

    # BROW
    "brow.T.R": ["brow.T.R", "FaceEmpty_143", 3,            brow_sides_influence],
    "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70", 3,     brow_sides_influence],
    "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107", 3,    brow_master_influence],
    "brow.B.R": ["brow.B.R", "FaceEmpty_247", 3,            brow_master_influence],
    "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30", 3,     brow_master_influence],
    "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27", 3,     brow_master_influence],
    "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56", 3,     brow_master_influence],

    "brow.T.L": ["brow.T.L", "FaceEmpty_372", 3,            brow_sides_influence],
    "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300", 3,    brow_sides_influence],
    "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336", 3,    brow_master_influence],
    "brow.B.L": ["brow.B.L", "FaceEmpty_467", 3,            brow_master_influence],
    "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260", 3,    brow_master_influence],
    "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257", 3,    brow_master_influence],
    "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286", 3,    brow_master_influence],

    # EYES
    "lid.T.R": ["lid.T.R", "FaceEmpty_33", 3,               lid_influence],
    "lid.T.R.001": ["lid.T.R.001", "FaceEmpty_161", 3,      lid_influence],
    "lid.T.R.002": ["lid.T.R.002", "FaceEmpty_159", 3,      lid_influence],
    "lid.T.R.003": ["lid.T.R.003", "FaceEmpty_157", 3,      lid_influence],
    "lid.B.R": ["lid.B.R", "FaceEmpty_133", 3,              lid_influence],
    "lid.B.R.001": ["lid.B.R.001", "FaceEmpty_154", 3,      lid_influence],
    "lid.B.R.002": ["lid.B.R.002", "FaceEmpty_145", 3,      lid_influence],
    "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_163", 3,      lid_influence],

    "lid.B.L": ["lid.B.L", "FaceEmpty_362", 3,              lid_influence],
    "lid.B.L.001": ["lid.B.L.001", "FaceEmpty_381", 3,      lid_influence],
    "lid.B.L.002": ["lid.B.L.002", "FaceEmpty_374", 3,      lid_influence],
    "lid.B.L.003": ["lid.B.L.003", "FaceEmpty_390", 3,      lid_influence],
    "lid.T.L": ["lid.T.L", "FaceEmpty_263", 3,              lid_influence],
    "lid.T.L.001": ["lid.T.L.001", "FaceEmpty_388", 3,      lid_influence],
    "lid.T.L.002": ["lid.T.L.002", "FaceEmpty_386", 3,      lid_influence],
    "lid.T.L.003": ["lid.T.L.003", "FaceEmpty_384", 3,      lid_influence],
}
"""

constrained_bones = {
    # JAW
    "jaw_master": ["jaw_master", "FaceEmpty_152", 23, 1],
    "jaw.L.001": ["jaw.L.001", "FaceEmpty_435", 3, 0.25],
    "jaw.R.001": ["jaw.R.001", "FaceEmpty_215", 3, 0.25],

    # CHIN
    "chin": ["chin", "FaceEmpty_152", 3, 1],
    "chin.R": ["chin.R", "FaceEmpty_32", 3, 0.75],
    "chin.L": ["chin.L", "FaceEmpty_262", 3, 0.75],

    # LIPS
    "lips.R": ["lips.R", "FaceEmpty_61", 3, 1],
    "lips.L": ["lips.L", "FaceEmpty_291", 3, 1],
    "lips.T": ["lips.T", "FaceEmpty_0", 3, 1],

    # NOSE
    "nose.L": ["nose.L", "FaceEmpty_437", 3, 0.5],
    "nose.L.001": ["nose.L.001", "FaceEmpty_358", 3, 0.5],
    "nose.R": ["nose.R", "FaceEmpty_217", 3, 0.5],
    "nose.R.001": ["nose.R.001", "FaceEmpty_129", 3, 0.5],

    # BROW
    "brow.T.R": ["brow.T.R", "FaceEmpty_143", 3, 0.25],
    "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70", 3, 0.25],
    "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107", 3, 0.75],
    "brow.B.R": ["brow.B.R", "FaceEmpty_247", 3, 0.75],
    "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30", 3, 0.75],
    "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27", 3, 0.75],
    "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56", 3, 0.75],

    "brow.T.L": ["brow.T.L", "FaceEmpty_372", 3, 0.25],
    "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300", 3, 0.25],
    "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336", 3, 0.75],
    "brow.B.L": ["brow.B.L", "FaceEmpty_467", 3, 0.75],
    "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260", 3, 0.75],
    "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257", 3, 0.75],
    "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286", 3, 0.75],

    # EYES
    "lid.T.R": ["lid.T.R", "FaceEmpty_33", 3, 0.75],
    "lid.T.R.001": ["lid.T.R.001", "FaceEmpty_161", 3, 0.75],
    "lid.T.R.002": ["lid.T.R.002", "FaceEmpty_159", 3, 0.75],
    "lid.T.R.003": ["lid.T.R.003", "FaceEmpty_157", 3, 0.75],
    "lid.B.R": ["lid.B.R", "FaceEmpty_133", 3, 0.75],
    "lid.B.R.001": ["lid.B.R.001", "FaceEmpty_154", 3, 0.75],
    "lid.B.R.002": ["lid.B.R.002", "FaceEmpty_145", 3, 0.75],
    "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_163", 3, 0.75],

    "lid.B.L": ["lid.B.L", "FaceEmpty_362", 3, 0.75],
    "lid.B.L.001": ["lid.B.L.001", "FaceEmpty_381", 3, 0.75],
    "lid.B.L.002": ["lid.B.L.002", "FaceEmpty_374", 3, 0.75],
    "lid.B.L.003": ["lid.B.L.003", "FaceEmpty_390", 3, 0.75],
    "lid.T.L": ["lid.T.L", "FaceEmpty_263", 3, 0.75],
    "lid.T.L.001": ["lid.T.L.001", "FaceEmpty_388", 3, 0.75],
    "lid.T.L.002": ["lid.T.L.002", "FaceEmpty_386", 3, 0.75],
    "lid.T.L.003": ["lid.T.L.003", "FaceEmpty_384", 3, 0.75],
}


def add_constraint(bone, data):
    constraints = {
        0: "CAMERA_SOLVER",
        1: "FOLLOW_TRACK",
        2: "OBJECT_SOLVER",
        3: "COPY_LOCATION",
        4: "COPY_ROTATION",
        5: "COPY_SCALE",
        6: "COPY_TRANSFORMS",
        7: "LIMIT_DISTANCE",
        8: "LIMIT_LOCATION",
        9: "LIMIT_ROTATION",
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


for bone in bones:

    try:
        data = constrained_bones[bone.name]
        add_constraint(bone, data)
        print(data)

    except KeyError:
        pass
