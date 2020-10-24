import json
import codecs
from main import poseDataHandler as pdh

jsonTypes = {
    "none": 0,
    "poseList": 1,
    "faceList": 2,
    "otherList": 3
}

# _____________________________________ VALIDATION __________________________________________

# validation of the incoming json


def validate_json(json_path):
    try:
        tmp = json.load(codecs.open(json_path, 'r', 'utf-8-sig'))
    except ValueError as err:
        return False
    return True


# analyzing the json data type


def get_json_type(json_data):
    for data in jsonTypes:
        if data in json_data:
            global CUR_TYPE
            CUR_TYPE = jsonTypes[data]


def start_validation(json_path):
    if validate_json(json_path):
        global JSON_DATA
        JSON_DATA = json.load(codecs.open(json_path, 'r', 'utf-8-sig'))
        get_json_type(JSON_DATA)
        print("received valid json input")
    else:
        print("given json is not valid")


# _____________________________________ IMPORT __________________________________________

def import_pose_data():
    pdh.init_pose_list(JSON_DATA)
    for data in pdh.POSE_LIST:
        data.print_content()


def start_import_process():
    if CUR_TYPE == 0:
        print("import pos data")
    elif CUR_TYPE == 1:
        import_pose_data()
    elif CUR_TYPE == 2:
        print("test")
