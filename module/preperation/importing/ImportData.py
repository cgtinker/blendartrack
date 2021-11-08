from . import InitDataTypes
from ..validation import ValidateJson
from ..pathing import Pathing

import importlib

importlib.reload(ValidateJson)
importlib.reload(Pathing)
importlib.reload(InitDataTypes)


def validate_json_data(data_path):
    valid_type, json_data = ValidateJson.is_json_valid(data_path)
    valid_contents = ValidateJson.is_json_iterable(data_path)
    return json_data, valid_contents, valid_type


def import_json_data(data_path):
    json_data, valid_contents, valid_type = validate_json_data(data_path)
    if valid_type is True and valid_contents is True:
        import_success = import_json_contents(json_data)
        return import_success

    else:
        return [], "", False


# init methods in ImportJson.py by string
def get_method_reference(json_data):
    json_title_string = {
        "none": InitDataTypes.none,
        "cameraPoseList": InitDataTypes.init_pose_model,
        "facePoseList": InitDataTypes.init_pose_model,

        "meshDataList": InitDataTypes.init_face_mesh_model,
        "meshGeometry": InitDataTypes.init_face_mesh_geo_model,
        "blendShapeData": InitDataTypes.init_blend_shape_model,
        "cameraProjection": InitDataTypes.init_camera_projection_model,

        "points": InitDataTypes.init_point_cloud_model,
        "anchorData": InitDataTypes.init_point_cloud_model,

        "screenPosData": InitDataTypes.init_screen_to_world_model
    }

    init_model = InitDataTypes.none
    title = ""

    for json_title in json_title_string:
        if json_title in json_data:
            init_model = json_title_string[json_title]
            title = json_title

    return init_model, title


def import_json_contents(json_data):
    init_model, title = get_method_reference(json_data)
    if init_model != InitDataTypes.none:
        model_data, is_imported = init_model(json_data, title)
        return model_data, title, is_imported

    else:
        print("Couldn't find a fitting import model")
        return [], "", False


def import_tracking_data(data_path):
    # check if the json has a valid formatting
    if Pathing.is_json_path(data_path):
        return import_json_data(data_path)

    elif Pathing.is_movie_path(data_path):
        model_data, valid = InitDataTypes.init_movie_model(data_path)
        return model_data, "movie", valid

    else:
        print("The given data is not valid.")
        return [], "", False
