from .models import PoseData, ScreenToWorldData, FaceMeshData, BlendShapeData, \
    CameraProjectionData, PointCloudData, MeshGeometryData, MovieData
from .models.helper import JsonValidator
from . import Pathing

import importlib

importlib.reload(PoseData)
importlib.reload(BlendShapeData)
importlib.reload(FaceMeshData)
importlib.reload(JsonValidator)
importlib.reload(CameraProjectionData)
importlib.reload(PointCloudData)
importlib.reload(ScreenToWorldData)
importlib.reload(MeshGeometryData)
importlib.reload(Pathing)
importlib.reload(MovieData)


def none(json_data, title):
    print(json_data, title)
    return ""


def init_pose_model(json_data, title):
    model_data = PoseData.init_pose_model(json_data, title)
    print("importing pose model data successful")
    return model_data, True


def init_screen_to_world_model(json_data, title):
    model_data = ScreenToWorldData.init_screen_to_world_model(json_data, title)
    print("importing pose model data successful")
    return model_data, True


def init_face_mesh_model(json_data, title):
    model_data = FaceMeshData.init_mesh_model(json_data, title)
    print("importing face mesh model data successful")
    return model_data, True


def init_face_mesh_geo_model(json_data, title):
    model_data = MeshGeometryData.init_mesh_geo_model(json_data, title)
    print("importing face mesh geometry model data successful")
    return model_data, True


def init_blend_shape_model(json_data, title):
    model_data = BlendShapeData.init_shape_model(json_data, title)
    print("importing blend shape data successful")
    return model_data, True


def init_camera_projection_model(json_data, title):
    model_data = CameraProjectionData.init_camera_projection_data(json_data, title)
    print("importing intrinsics data successful")
    return model_data, True


def init_point_cloud_model(json_data, title):
    model_data = PointCloudData.init_point_cloud(json_data, title)
    print("importing", title, "successful")
    return model_data, True


def init_movie_model(data_path):
    model_data = MovieData.init_movie_data(data_path)
    print("importing movie data successful")
    return model_data, True


def import_retargeter_data(data_path):
    # check if the json has a valid formatting
    if Pathing.is_json_path(data_path):
        valid_json, json_data = JsonValidator.validate_json(data_path)
        if valid_json:
            # every json contains a title string for reference
            json_title_string = {
                "none": none,
                "cameraPoseList": init_pose_model,
                "facePoseList": init_pose_model,

                "meshDataList": init_face_mesh_model,
                "meshGeometry": init_face_mesh_geo_model,
                "blendShapeData": init_blend_shape_model,
                "cameraProjection": init_camera_projection_model,

                "points": init_point_cloud_model,
                "anchorData": init_point_cloud_model,

                "screenPosData": init_screen_to_world_model
            }

            # generating model data
            import_model, title = get_method_reference(json_title_string, json_data)
            if import_model != none:
                model_data, valid = import_model(json_data, title)
                return model_data, title, valid

            else:
                print("Couldn't find a fitting import model")
                return [], "", False

    else:
        if Pathing.is_movie_path(data_path):
            model_data, valid = init_movie_model(data_path)
            return model_data, "movie", valid

        else:
            print("The given data is not valid.")
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
