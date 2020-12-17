from .models import PoseData, ScreenToWorldData, FaceMeshData, BlendShapeData, CameraProjectionData, PointCloudData
from .models.helper import JsonValidator
from . import ExecuteModel

import importlib

importlib.reload(PoseData)
importlib.reload(BlendShapeData)
importlib.reload(FaceMeshData)
importlib.reload(JsonValidator)
importlib.reload(CameraProjectionData)
importlib.reload(PointCloudData)
importlib.reload(ScreenToWorldData)


def none(json_data, title):
    print(json_data, title)
    return ""


def init_pose_model(json_data, title):
    model_data = PoseData.init_pose_model(json_data, title)
    print("importing pose model data successful")
    # ExecuteModel.exec_pose_data(model_data)
    return model_data, True


def init_screen_to_world_model(json_data, title):
    model_data = ScreenToWorldData.init_screen_to_world_model(json_data, title)
    print("importing pose model data successful")
    # ExecuteModel.exec_screen_to_world_data(model_data)
    return model_data, True


def init_face_mesh_model(json_data, title):
    model_data = FaceMeshData.init_mesh_model(json_data, title)
    print("importing face mesh model data successful")
    # ExecuteModel.exec_face_mesh(model_data)
    return model_data, True


# this is not used!
def init_planes(json_data, title):
    for data in json_data['objectToTrack']:
        init_pose_model(data, title)
    return ""


def init_blend_shape_model(json_data, title):
    model_data = BlendShapeData.init_shape_model(json_data, title)
    print("importing blend shape data successful")
    # ExecuteModel.exec_shape_keys(model_data)
    return model_data, True


def init_camera_projection_model(json_data, title):
    model_data = CameraProjectionData.init_camera_intrinsics_data(json_data, title)
    print("importing intrinsics data successful")
    # ExecuteModel.exec_projection_data(model_data)
    return model_data, True


def init_point_cloud_model(json_data, title):
    model_data = PointCloudData.init_point_cloud(json_data, title)
    print("importing", title, "successful")
    # ExecuteModel.exec_point_cloud_data(model_data)
    return model_data, True


def import_json_data(json_path):
    # check if the json has a valid formatting
    valid_json, json_data = JsonValidator.validate_json(json_path)
    if valid_json:
        # every json contains a title string for reference
        json_title_string = {
            "none": none,
            "cameraPoseList": init_pose_model,
            "facePoseList": init_pose_model,

            "meshDataList": init_face_mesh_model,
            "blendShapeData": init_blend_shape_model,
            "cameraProjection": init_camera_projection_model,

            "points": init_point_cloud_model,
            "anchorData": init_point_cloud_model,

            "screenPosData": init_screen_to_world_model
        }

        # print("Json is valid, checking Data Type.")
        import_model, title = get_method_reference(json_title_string, json_data)

        if import_model != none:
            model_data, valid = import_model(json_data, title)
            return model_data, title, valid

        else:
            print("Couldn't find a fitting import model")
            return [], "", False
    else:
        print("The given json is not valid.")
        return [], "", False


def get_method_reference(json_title_string, json_data):
    import_model = none
    title = ""

    for json_title in json_title_string:
        if json_title in json_data:
            # get function title by the reference title in the data
            import_model = json_title_string[json_title]
            title = json_title

    return import_model, title
