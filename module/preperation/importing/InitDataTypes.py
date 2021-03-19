from module.data_types import MeshGeometryData, PoseData, PointCloudData, FaceMeshData, MovieData, \
    BlendShapeData
from module.data_types import ScreenToWorldData, CameraProjectionData

import importlib
import sys
importlib.reload(PoseData)
importlib.reload(BlendShapeData)
importlib.reload(FaceMeshData)
importlib.reload(CameraProjectionData)
importlib.reload(PointCloudData)
importlib.reload(ScreenToWorldData)
importlib.reload(MeshGeometryData)
importlib.reload(MovieData)


def none(json_data, title):
    print(json_data, title)
    return ""


def init_pose_model(json_data, title):
    try:
        model_data = PoseData.init_pose_model(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_screen_to_world_model(json_data, title):
    try:
        model_data = ScreenToWorldData.init_screen_to_world_model(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_face_mesh_model(json_data, title):
    try:
        model_data = FaceMeshData.init_mesh_model(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_face_mesh_geo_model(json_data, title):
    try:
        model_data = MeshGeometryData.init_mesh_geo_model(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_blend_shape_model(json_data, title):
    try:
        model_data = BlendShapeData.init_shape_model(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_camera_projection_model(json_data, title):
    try:
        model_data = CameraProjectionData.init_camera_projection_data(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_point_cloud_model(json_data, title):
    try:
        model_data = PointCloudData.init_point_cloud(json_data, title)
    except TypeError:
        return expect_failure(title)
    return success(title, model_data)


def init_movie_model(data_path):
    try:
        model_data = MovieData.init_movie_data(data_path)
    except TypeError:
        return expect_failure("movie")
    return success("movie", model_data)


def success(title, model_data):
    print(title, "imported successfully")
    return model_data, True


def expect_failure(title):
    e = sys.exc_info()[0]
    print(title, "cannot be imported: ", e)
    return "", False
