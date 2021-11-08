# raw shape key names based on ios face tracking in order
ref_dict = {
    "EyeBlinkRight": 0,
    "EyeWideRight": 1,
    "MouthLowerDownLeft": 2,
    "MouthRollUpper": 3,
    "CheekSquintLeft": 4,
    "MouthDimpleRight": 5,
    "BrowInnerUp": 6,
    "EyeLookInLeft": 7,
    "MouthPressLeft": 8,
    "MouthStretchRight": 9,
    "BrowDownLeft": 10,
    "MouthFunnel": 11,
    "NoseSneerLeft": 12,
    "EyeLookOutLeft": 13,
    "EyeLookInRight": 14,
    "MouthLowerDownRight": 15,
    "BrowOuterUpRight": 16,
    "MouthLeft": 17,
    "CheekSquintRight": 18,
    "JawOpen": 19,
    "EyeBlinkLeft": 20,
    "JawForward": 21,
    "MouthPressRight": 22,
    "NoseSneerRight": 23,
    "JawRight": 24,
    "MouthShrugLower": 25,
    "EyeSquintLeft": 26,
    "EyeLookOutRight": 27,
    "MouthFrownLeft": 28,
    "CheekPuff": 29,
    "MouthStretchLeft": 30,
    "TongueOut": 31,
    "MouthRollLower": 32,
    "MouthUpperUpRight": 33,
    "MouthShrugUpper": 34,
    "EyeSquintRight": 35,
    "EyeLookDownLeft": 36,
    "MouthSmileLeft": 37,
    "EyeWideLeft": 38,
    "MouthClose": 39,
    "JawLeft": 40,
    "MouthDimpleLeft": 41,
    "MouthFrownRight": 42,
    "MouthPucker": 43,
    "MouthRight": 44,
    "EyeLookUpLeft": 45,
    "BrowDownRight": 46,
    "MouthSmileRight": 47,
    "MouthUpperUpLeft": 48,
    "BrowOuterUpLeft": 49,
    "EyeLookUpRight": 50,
    "EyeLookDownRight": 51
}


# changing the value of the dict depending on the input name
def set_blend_shape_reference(name, value):
    ref_dict[name] = value  # value = selected obj shape key index


# getting the reference name in the dict, depending on the mapped name
def get_shape_key_reference(name, obj_keys):
    index = generate_shape_key_index(name, obj_keys)
    return index


def generate_shape_key_index(name, obj_keys):
    if len(obj_keys) <= 0:  # obj has to include shape keys
        return

    index = -1  # default value = -1 for missing keys
    for i in range(len(obj_keys)):  # shape key name + index as output
        if obj_keys[i].name == name:
            index = i

    return index


def blend_to_shape_key_mapping(obj_keys):
    set_blend_shape_reference("BrowDownLeft", get_shape_key_reference("browDown_L", obj_keys))
    set_blend_shape_reference("BrowDownRight", get_shape_key_reference("browDown_R", obj_keys))
    set_blend_shape_reference("BrowInnerUp", get_shape_key_reference("browInnerUp", obj_keys))
    set_blend_shape_reference("BrowOuterUpLeft", get_shape_key_reference("browOuterUp_L", obj_keys))
    set_blend_shape_reference("BrowOuterUpRight", get_shape_key_reference("browOuterUp_R", obj_keys))
    set_blend_shape_reference("CheekPuff", get_shape_key_reference("cheekPuff", obj_keys))
    set_blend_shape_reference("CheekSquintLeft", get_shape_key_reference("cheekSquint_L", obj_keys))
    set_blend_shape_reference("CheekSquintRight", get_shape_key_reference("cheekSquint_R", obj_keys))
    set_blend_shape_reference("EyeBlinkLeft", get_shape_key_reference("eyeBlink_L", obj_keys))
    set_blend_shape_reference("EyeBlinkRight", get_shape_key_reference("eyeBlink_R", obj_keys))
    set_blend_shape_reference("EyeLookDownLeft", get_shape_key_reference("eyeLookDown_L", obj_keys))
    set_blend_shape_reference("EyeLookDownRight", get_shape_key_reference("eyeLookDown_R", obj_keys))
    set_blend_shape_reference("EyeLookInLeft", get_shape_key_reference("eyeLookIn_L", obj_keys))
    set_blend_shape_reference("EyeLookInRight", get_shape_key_reference("eyeLookIn_R", obj_keys))
    set_blend_shape_reference("EyeLookOutLeft", get_shape_key_reference("eyeLookOut_L", obj_keys))
    set_blend_shape_reference("EyeLookOutRight", get_shape_key_reference("eyeLookOut_R", obj_keys))
    set_blend_shape_reference("EyeLookUpLeft", get_shape_key_reference("eyeLookUp_L", obj_keys))
    set_blend_shape_reference("EyeLookUpRight", get_shape_key_reference("eyeLookUp_R", obj_keys))
    set_blend_shape_reference("EyeSquintLeft", get_shape_key_reference("eyeSquint_L", obj_keys))
    set_blend_shape_reference("EyeSquintRight", get_shape_key_reference("eyeSquint_R", obj_keys))
    set_blend_shape_reference("EyeWideLeft", get_shape_key_reference("eyeWide_L", obj_keys))
    set_blend_shape_reference("EyeWideRight", get_shape_key_reference("eyeWide_R", obj_keys))
    set_blend_shape_reference("JawForward", get_shape_key_reference("jawForward", obj_keys))
    set_blend_shape_reference("JawLeft", get_shape_key_reference("jawLeft", obj_keys))
    set_blend_shape_reference("JawOpen", get_shape_key_reference("jawOpen", obj_keys))
    set_blend_shape_reference("JawRight", get_shape_key_reference("jawRight", obj_keys))
    set_blend_shape_reference("MouthClose", get_shape_key_reference("mouthClose", obj_keys))
    set_blend_shape_reference("MouthDimpleLeft", get_shape_key_reference("mouthDimple_L", obj_keys))
    set_blend_shape_reference("MouthDimpleRight", get_shape_key_reference("mouthDimple_R", obj_keys))
    set_blend_shape_reference("MouthFrownLeft", get_shape_key_reference("mouthFrown_L", obj_keys))
    set_blend_shape_reference("MouthFrownRight", get_shape_key_reference("mouthFrown_R", obj_keys))
    set_blend_shape_reference("MouthFunnel", get_shape_key_reference("mouthFunnel", obj_keys))
    set_blend_shape_reference("MouthLeft", get_shape_key_reference("mouthLeft", obj_keys))
    set_blend_shape_reference("MouthLowerDownLeft", get_shape_key_reference("mouthLowerDown_L", obj_keys))
    set_blend_shape_reference("MouthLowerDownRight", get_shape_key_reference("mouthLowerDown_R", obj_keys))
    set_blend_shape_reference("MouthPressLeft", get_shape_key_reference("mouthPress_L", obj_keys))
    set_blend_shape_reference("MouthPressRight", get_shape_key_reference("mouthPress_R", obj_keys))
    set_blend_shape_reference("MouthPucker", get_shape_key_reference("mouthPucker", obj_keys))
    set_blend_shape_reference("MouthRight", get_shape_key_reference("mouthRight", obj_keys))
    set_blend_shape_reference("MouthRollLower", get_shape_key_reference("mouthRollLower", obj_keys))
    set_blend_shape_reference("MouthRollUpper", get_shape_key_reference("mouthRollUpper", obj_keys))
    set_blend_shape_reference("MouthShrugLower", get_shape_key_reference("mouthShrugLower", obj_keys))
    set_blend_shape_reference("MouthShrugUpper", get_shape_key_reference("mouthShrugUpper", obj_keys))
    set_blend_shape_reference("MouthSmileLeft", get_shape_key_reference("mouthSmile_L", obj_keys))
    set_blend_shape_reference("MouthSmileRight", get_shape_key_reference("mouthSmile_R", obj_keys))
    set_blend_shape_reference("MouthStretchLeft", get_shape_key_reference("mouthStretch_L", obj_keys))
    set_blend_shape_reference("MouthStretchRight", get_shape_key_reference("mouthStretch_R", obj_keys))
    set_blend_shape_reference("MouthUpperUpLeft", get_shape_key_reference("mouthUpperUp_L", obj_keys))
    set_blend_shape_reference("MouthUpperUpRight", get_shape_key_reference("mouthUpperUp_R", obj_keys))
    set_blend_shape_reference("NoseSneerLeft", get_shape_key_reference("noseSneer_L", obj_keys))
    set_blend_shape_reference("NoseSneerRight", get_shape_key_reference("noseSneer_R", obj_keys))
    set_blend_shape_reference("TongueOut", get_shape_key_reference("tongueOut", obj_keys))


def create_blend_shape_mapping(obj_keys):   # input = shape key names from selected obj
    blend_to_shape_key_mapping(obj_keys)
    return ref_dict
