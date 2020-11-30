from .models import PoseData, FaceMeshData, BlendShapeData, CameraProjectionData, PointCloudData
from .models.helper import JsonValidator
from . import ExecuteModel

import importlib

importlib.reload(PoseData)
importlib.reload(BlendShapeData)
importlib.reload(FaceMeshData)
importlib.reload(JsonValidator)
importlib.reload(CameraProjectionData)
importlib.reload(PointCloudData)


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


def init_camera_projection_model(json_data):
    model_data = CameraProjectionData.init_camera_intrinsics_data(json_data)
    print("importing intrinsics data successful")
    ExecuteModel.exec_projection_data(model_data)


def init_point_cloud_model(json_data):
    model_data = PointCloudData.init_point_cloud(json_data)
    print("importing point cloud data successful")
    ExecuteModel.exec_point_cloud_data(model_data)


def import_json_data(json_path):
    # check if the json has a valid formatting
    valid_json, json_data = JsonValidator.validate_json(json_path)
    if valid_json:
        # every json contains a title string for reference
        json_title_string = {
            "nullOrEmpty": none,
            "cameraPoseList": init_pose_model,
            "meshDataList": init_face_mesh_model,
            "blendShapeData": init_blend_shape_model,
            "cameraProjection": init_camera_projection_model,
            "points": init_point_cloud_model
        }

        print("Json is valid, checking Data Type.")
        import_model = get_method_reference(json_title_string, json_data)

        if import_model != none:
            import_model(json_data)

        else:
            print("Couldn't find a fitting import model")
    else:
        print("The given json is not valid.")


def get_method_reference(json_title_string, json_data):
    import_model = none

    for json_title in json_title_string:
        if json_title in json_data:
            print("Imported data type:", json_title)
            # get function title by the reference title in the data
            import_model = json_title_string[json_title]

    return import_model
