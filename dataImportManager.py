from main import poseDataHandler as pdh


# _____________________________________ IMPORTER DEFs __________________________________________ #

def none():
    print("0")
    return "zero"


def import_pose_data(JSON_DATA):
    CUR_DATA = pdh.init_pose_list(JSON_DATA)
    return CUR_DATA


def import_face_mesh():
    print("2")
    return "two"


def import_shape_keys():
    print("3")
    return "three"

# _____________________________________ REF DICTs __________________________________________ #


json_titles = {
    "none": 0,
    "poseList": 1,
    "faceMesh": 2,
    "shapeKeys": 3
}

json_def = {
    0: none,
    1: import_pose_data,
    2: import_face_mesh,
    3: import_shape_keys
}


# _____________________________________ ANALYSE DATA __________________________________________


# analyzing the json data type
def json_data_type(JSON_DATA):
    for data in json_titles:
        if data in JSON_DATA:
            global CUR_TYPE
            CUR_TYPE = json_titles[data]
            return CUR_TYPE


def return_received_data(CUR_TYPE, JSON_DATA):
    # get the function by a (int) current type
    func = json_def.get(CUR_TYPE, JSON_DATA)
    # create a reference of the current data
    CUR_DATA = func(JSON_DATA)
    return CUR_DATA
