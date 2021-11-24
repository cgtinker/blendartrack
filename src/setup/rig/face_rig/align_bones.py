from src.utils.blend import objects, viewport, armature
from src.utils.blend import user

head_ref = {
    "chin": ["chin", "FaceEmpty_152"],
    "chin.001": ["chin.001", "FaceEmpty_199"],
    "nose": ["nose", "FaceEmpty_168"],
    "nose.001": ["nose.001", "FaceEmpty_5"],
    "nose.002": ["nose.002", "FaceEmpty_4"],
    "nose.003": ["nose.003", "FaceEmpty_19"],
    "nose.004": ["nose.004", "FaceEmpty_94"],

    "temple.L": ["temple.L", "FaceEmpty_251"],
    "jaw.L": ["jaw.L", "FaceEmpty_447"],
    "jaw.L.001": ["jaw.L.001", "FaceEmpty_435"],

    "chin.L": ["chin.L", "FaceEmpty_262"],

    "nose.L": ["nose.L", "FaceEmpty_437"],
    "nose.L.001": ["nose.L.001", "FaceEmpty_358"],

    "cheek.T.L": ["cheek.T.L", "FaceEmpty_372"],
    "cheek.T.L.001": ["cheek.T.L.001", "FaceEmpty_425"],
    "cheek.B.L": ["cheek.B.L", "FaceEmpty_291"],
    "cheek.B.L.001": ["cheek.B.L.001", "FaceEmpty_411"],

    "brow.T.L": ["brow.T.L", "FaceEmpty_372"],
    "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300"],
    "brow.T.L.002": ["brow.T.L.002", "FaceEmpty_334"],
    "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336"],

    "forehead.L": ["forehead.L", "FaceEmpty_338"],
    "forehead.L.001": ["forehead.L.001", "FaceEmpty_297"],
    "forehead.L.002": ["forehead.L.002", "FaceEmpty_332"],

    "lip.T.L": ["lip.T.L", "FaceEmpty_0"],
    "lip.T.L.001": ["lip.T.L.001", "FaceEmpty_269"],
    "lip.B.L": ["lip.B.L", "FaceEmpty_17"],
    "lip.B.L.001": ["lip.B.L.001", "FaceEmpty_405"],

    "brow.B.L": ["brow.B.L", "FaceEmpty_467"],
    "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260"],
    "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257"],
    "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286"],

    "lid.B.L": ["lid.B.L", "FaceEmpty_362"],
    "lid.B.L.001": ["lid.B.L.001", "FaceEmpty_381"],
    "lid.B.L.002": ["lid.B.L.002", "FaceEmpty_374"],
    "lid.B.L.003": ["lid.B.L.003", "FaceEmpty_390"],
    "lid.T.L": ["lid.T.L", "FaceEmpty_263"],
    "lid.T.L.001": ["lid.T.L.001", "FaceEmpty_388"],
    "lid.T.L.002": ["lid.T.L.002", "FaceEmpty_386"],
    "lid.T.L.003": ["lid.T.L.003", "FaceEmpty_384"],

    "nose.R": ["nose.R", "FaceEmpty_217"],
    "nose.R.001": ["nose.R.001", "FaceEmpty_129"],
    "cheek.T.R": ["cheek.T.R", "FaceEmpty_143"],
    "cheek.T.R.001": ["cheek.T.R.001", "FaceEmpty_205"],

    "temple.R": ["temple.R", "FaceEmpty_21"],
    "jaw.R": ["jaw.R", "FaceEmpty_227"],
    "jaw.R.001": ["jaw.R.001", "FaceEmpty_215"],

    "chin.R": ["chin.R", "FaceEmpty_32"],
    "cheek.B.R": ["cheek.B.R", "FaceEmpty_61"],
    "cheek.B.R.001": ["cheek.B.R.001", "FaceEmpty_187"],

    "brow.T.R": ["brow.T.R", "FaceEmpty_143"],
    "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70"],
    "brow.T.R.002": ["brow.T.R.002", "FaceEmpty_105"],
    "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107"],

    "forehead.R": ["forehead.R", "FaceEmpty_109"],
    "forehead.R.001": ["forehead.R.001", "FaceEmpty_67"],
    "forehead.R.002": ["forehead.R.002", "FaceEmpty_103"],

    "lip.T.R": ["lip.T.R", "FaceEmpty_0"],
    "lip.T.R.001": ["lip.T.R.001", "FaceEmpty_39"],
    "lip.B.R": ["lip.B.R", "FaceEmpty_17"],
    "lip.B.R.001": ["lip.B.R.001", "FaceEmpty_181"],

    "lid.T.R": ["lid.T.R", "FaceEmpty_33"],
    "lid.T.R.001": ["lid.T.R.001", "FaceEmpty_161"],
    "lid.T.R.002": ["lid.T.R.002", "FaceEmpty_159"],
    "lid.T.R.003": ["lid.T.R.003", "FaceEmpty_157"],
    "lid.B.R": ["lid.B.R", "FaceEmpty_133"],
    "lid.B.R.001": ["lid.B.R.001", "FaceEmpty_154"],
    "lid.B.R.002": ["lid.B.R.002", "FaceEmpty_145"],
    "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_163"],

    "brow.B.R": ["brow.B.R", "FaceEmpty_247"],
    "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30"],
    "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27"],
    "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56"],
}

tail_ref = {
    "nose.L.001": ["nose.L.001", "FaceEmpty_4"],
    "nose.R.001": ["nose.R.001", "FaceEmpty_4"],
    "chin.001": ["chin.001", "FaceEmpty_18"],
    "lip.T.L.001": ["lip.T.L.001", "FaceEmpty_291"],
    "lip.B.L.001": ["lip.B.L.001", "FaceEmpty_291"],
    "lip.T.R.001": ["lip.T.R.001", "FaceEmpty_61"],
    "lip.B.R.001": ["lip.B.R.001", "FaceEmpty_61"],
    "forehead.R": ["forehead.R", "FaceEmpty_107"],
    "forehead.R.001": ["forehead.R.001", "FaceEmpty_105"],
    "forehead.R.002": ["forehead.R.002", "FaceEmpty_70"],

    "forehead.L": ["forehead.L", "FaceEmpty_336"],
    "forehead.L.001": ["forehead.L.001", "FaceEmpty_334"],
    "forehead.L.002": ["forehead.L.002", "FaceEmpty_300"],

    "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_168"],
    "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_414"],
    "lid.B.L.003": ["brow.T.L.003", "FaceEmpty_263"],

    "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_168"],
    "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_190"],
    "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_33"],
}


ios_head_ref = {
    'chin': ['chin', 'FaceEmpty_1047'],
    'chin.001': ['chin.001', 'FaceEmpty_975'],
    'nose': ['nose', 'FaceEmpty_36'],
    'nose.001': ['nose.001', 'FaceEmpty_10'],
    'nose.002': ['nose.002', 'FaceEmpty_8'],
    'nose.003': ['nose.003', 'FaceEmpty_37'],
    'nose.004': ['nose.004', 'FaceEmpty_4'],
    'temple.L': ['temple.L', 'FaceEmpty_579'],
    'jaw.L': ['jaw.L', 'FaceEmpty_1008'],
    'jaw.L.001': ['jaw.L.001', 'FaceEmpty_1004'],
    'chin.L': ['chin.L', 'FaceEmpty_1050'],
    'nose.L': ['nose.L', 'FaceEmpty_609'],
    'nose.L.001': ['nose.L.001', 'FaceEmpty_865'],
    'cheek.T.L': ['cheek.T.L', 'FaceEmpty_670'],
    'cheek.T.L.001': ['cheek.T.L.001', 'FaceEmpty_600'],
    'cheek.B.L': ['cheek.B.L', 'FaceEmpty_622'],
    'cheek.B.L.001': ['cheek.B.L.001', 'FaceEmpty_885'],
    'brow.T.L': ['brow.T.L', 'FaceEmpty_670'],
    'brow.T.L.001': ['brow.T.L.001', 'FaceEmpty_648'],
    'brow.T.L.002': ['brow.T.L.002', 'FaceEmpty_657'],
    'brow.T.L.003': ['brow.T.L.003', 'FaceEmpty_781'],
    'forehead.L': ['forehead.L', 'FaceEmpty_853'],
    'forehead.L.001': ['forehead.L.001', 'FaceEmpty_580'],
    'forehead.L.002': ['forehead.L.002', 'FaceEmpty_660'],
    'lip.T.L': ['lip.T.L', 'FaceEmpty_1'],
    'lip.T.L.001': ['lip.T.L.001', 'FaceEmpty_547'],
    'lip.B.L': ['lip.B.L', 'FaceEmpty_29'],
    'lip.B.L.001': ['lip.B.L.001', 'FaceEmpty_714'],
    'brow.B.L': ['brow.B.L', 'FaceEmpty_1130'],
    'brow.B.L.001': ['brow.B.L.001', 'FaceEmpty_1128'],
    'brow.B.L.002': ['brow.B.L.002', 'FaceEmpty_1126'],
    'brow.B.L.003': ['brow.B.L.003', 'FaceEmpty_1124'],
    'lid.B.L': ['lid.B.L', 'FaceEmpty_1081'],
    'lid.B.L.001': ['lid.B.L.001', 'FaceEmpty_1084'],
    'lid.B.L.002': ['lid.B.L.002', 'FaceEmpty_1062'],
    'lid.B.L.003': ['lid.B.L.003', 'FaceEmpty_1064'],
    'lid.T.L': ['lid.T.L', 'FaceEmpty_1180'],
    'lid.T.L.001': ['lid.T.L.001', 'FaceEmpty_1073'],
    'lid.T.L.002': ['lid.T.L.002', 'FaceEmpty_1075'],
    'lid.T.L.003': ['lid.T.L.003', 'FaceEmpty_1078'],
    'nose.R': ['nose.R', 'FaceEmpty_160'],
    'nose.R.001': ['nose.R.001', 'FaceEmpty_437'],
    'cheek.T.R': ['cheek.T.R', 'FaceEmpty_235'],
    'cheek.T.R.001': ['cheek.T.R.001', 'FaceEmpty_151'],
    'temple.R': ['temple.R', 'FaceEmpty_130'],
    'jaw.R': ['jaw.R', 'FaceEmpty_939'],
    'jaw.R.001': ['jaw.R.001', 'FaceEmpty_927'],
    'chin.R': ['chin.R', 'FaceEmpty_986'],
    'cheek.B.R': ['cheek.B.R', 'FaceEmpty_173'],
    'cheek.B.R.001': ['cheek.B.R.001', 'FaceEmpty_457'],
    'brow.T.R': ['brow.T.R', 'FaceEmpty_235'],
    'brow.T.R.001': ['brow.T.R.001', 'FaceEmpty_199'],
    'brow.T.R.002': ['brow.T.R.002', 'FaceEmpty_209'],
    'brow.T.R.003': ['brow.T.R.003', 'FaceEmpty_348'],
    'forehead.R': ['forehead.R', 'FaceEmpty_425'],
    'forehead.R.001': ['forehead.R.001', 'FaceEmpty_131'],
    'forehead.R.002': ['forehead.R.002', 'FaceEmpty_212'],
    'lip.T.R': ['lip.T.R', 'FaceEmpty_1'],
    'lip.T.R.001': ['lip.T.R.001', 'FaceEmpty_98'],
    'lip.B.R': ['lip.B.R', 'FaceEmpty_29'],
    'lip.B.R.001': ['lip.B.R.001', 'FaceEmpty_279'],
    'lid.T.R': ['lid.T.R', 'FaceEmpty_1181'],
    'lid.T.R.001': ['lid.T.R.001', 'FaceEmpty_1097'],
    'lid.T.R.002': ['lid.T.R.002', 'FaceEmpty_1095'],
    'lid.T.R.003': ['lid.T.R.003', 'FaceEmpty_1092'],
    'lid.B.R': ['lid.B.R', 'FaceEmpty_1089'],
    'lid.B.R.001': ['lid.B.R.001', 'FaceEmpty_1086'],
    'lid.B.R.002': ['lid.B.R.002', 'FaceEmpty_1108'],
    'lid.B.R.003': ['lid.B.R.003', 'FaceEmpty_1106'],
    'brow.B.R': ['brow.B.R', 'FaceEmpty_1156'],
    'brow.B.R.001': ['brow.B.R.001', 'FaceEmpty_1154'],
    'brow.B.R.002': ['brow.B.R.002', 'FaceEmpty_1152'],
    'brow.B.R.003': ['brow.B.R.003', 'FaceEmpty_1150'],
}


ios_tail_ref = {
    'nose.L.001': ['nose.L.001', 'FaceEmpty_8'],
    'nose.R.001': ['nose.R.001', 'FaceEmpty_8'],
    'chin.001': ['chin.001', 'FaceEmpty_31'],
    'lip.T.L.001': ['lip.T.L.001', 'FaceEmpty_622'],
    'lip.B.L.001': ['lip.B.L.001', 'FaceEmpty_622'],
    'lip.T.R.001': ['lip.T.R.001', 'FaceEmpty_173'],
    'lip.B.R.001': ['lip.B.R.001', 'FaceEmpty_173'],
    'forehead.R': ['forehead.R', 'FaceEmpty_348'],
    'forehead.R.001': ['forehead.R.001', 'FaceEmpty_209'],
    'forehead.R.002': ['forehead.R.002', 'FaceEmpty_199'],
    'forehead.L': ['forehead.L', 'FaceEmpty_781'],
    'forehead.L.001': ['forehead.L.001', 'FaceEmpty_657'],
    'forehead.L.002': ['forehead.L.002', 'FaceEmpty_648'],
    'brow.T.L.003': ['brow.T.L.003', 'FaceEmpty_36'],
    'brow.B.L.003': ['brow.B.L.003', 'FaceEmpty_1123'],
    'lid.B.L.003': ['brow.T.L.003', 'FaceEmpty_1180'],
    'brow.T.R.003': ['brow.T.R.003', 'FaceEmpty_36'],
    'brow.B.R.003': ['brow.B.R.003', 'FaceEmpty_1149'],
    'lid.B.R.003': ['lid.B.R.003', 'FaceEmpty_1181'],
}


def get_bones(arm):
    objects.select_object(arm)
    viewport.set_edit_mode()
    bones = armature.get_armature_edit_bones(arm)
    return bones


def align_bone_head(bones, ref_dict, arm):
    for bone in bones:
        try:
            ref_name = ref_dict[bone.name][1]
            ob = objects.get_object(ref_name)
            bone.head = ob.location - arm.location

        except KeyError:
            pass


def align_bone_tail(bones, ref_dict, arm):
    for bone in bones:
        try:
            ref_name = ref_dict[bone.name][1]
            ob = objects.get_object(ref_name)
            bone.tail = ob.location - arm.location

        except KeyError:
            pass


def align(arm):
    bones = get_bones(arm)
    if user.get_user().enum_device_type == "Android":
        align_bone_head(bones, head_ref, arm)
        align_bone_tail(bones, tail_ref, arm)

    else:
        align_bone_head(bones, ios_head_ref, arm)
        align_bone_tail(bones, ios_tail_ref, arm)
    viewport.set_object_mode()



