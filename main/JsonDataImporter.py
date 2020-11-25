from main.models import PoseData, FaceMeshData, BlendShapeData
from main.helper import JsonValidator
from main import ExecuteModel

import importlib
importlib.reload(PoseData)
importlib.reload(BlendShapeData)
importlib.reload(FaceMeshData)
importlib.reload(JsonValidator)


def none():
    print("0")


def init_pose_model(json_data):
    model_data = PoseData.init_pose_model(json_data)
    print("importing pose model data successful")
    ExecuteModel.exec_pose_data(model_data)


def init_face_mesh_model(json_data):
    model_data = FaceMeshData.init_mesh_model(json_data)
    print("importing face mesh model data successful")
    ExecuteModel.exec_face_mesh(model_data)


def init_blend_shape_model(json_data):
    model_data = BlendShapeData.init_shape_model(json_data)
    print("importing blend shape data successful")
    ExecuteModel.exec_shape_keys(model_data)


def import_json_data(json_path):
    # check if the json has a valid formatting
    valid_json, json_data = JsonValidator.validate_json(json_path)
    if valid_json:
        # every json contains a title string for reference
        json_title_string = {
            "nullOrEmpty": none,
            "poseList": init_pose_model,
            "meshDataList": init_face_mesh_model,
            "blendShapeData": init_blend_shape_model
        }
        print("Json is valid, checking Data Type.")

        for json_title in json_title_string:
            if json_title in json_data:
                print("Imported data type:", json_title)
                # get function title by the reference title in the data
                import_model = json_title_string[json_title]
                import_model(json_data)
    else:
        print("The given json is not valid.")
