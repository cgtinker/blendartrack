import json
import codecs
from main.models import poseData as pdh


def none():
    print("0")
    return "zero"


def import_pose_data(json_data):
    cur_data = pdh.init_pose_list(json_data)
    return cur_data


def import_face_mesh():
    print("2")
    return "two"


def import_shape_keys():
    print("3")
    return "three"


def validate_json(json_path):
    try:
        json_data = json.load(codecs.open(json_path, 'r', 'utf-8-sig'))
    except ValueError as err:
        return False
    return True, json_data


def import_valid_json(json_path):
    valid_json, json_data = validate_json(json_path)
    if valid_json:
        received_data = import_json_data(json_data)
        return received_data
    else:
        print("given json is not valid")


def import_json_data(json_data):
    # every json contains a title string for reference
    json_title_string = {
        "none": none,
        "poseList": import_pose_data,
        "none": import_face_mesh,
        "none": import_shape_keys
    }

    # importing json data as model
    for m_string in json_title_string:
        if m_string in json_data:
            # get function title
            m_function = json_title_string[m_string]
            received_data = m_function(json_data)
            return received_data
