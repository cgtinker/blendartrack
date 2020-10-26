from main.models import PoseData
from main.helper import JsonValidator
from main import ModelRunner


def none():
    print("0")
    return "zero"


def init_pose_model(json_data):
    model_data = PoseData.init_pose_model(json_data)
    ModelRunner.exec_pose_data(model_data)
    return model_data


def init_face_model():
    print("2")
    return "two"


def init_key_model():
    print("3")
    return "three"


def import_json_data(json_path):
    # check if the json has a valid formatting
    valid_json, json_data = JsonValidator.validate_json(json_path)

    if valid_json:
        # every json contains a title string for reference
        json_title_string = {
            "a": none,
            "poseList": init_pose_model,
            "v": init_face_model,
            "none": init_key_model
        }

        for json_title in json_title_string:
            if json_title in json_data:
                # get function title by the reference title in the data
                import_model = json_title_string[json_title]
                model_data = import_model(json_data)
                return model_data
    else:
        print("The given json is not valid.")
