import json
import codecs


# validation of the incoming json
def validate_json(json_path):
    try:
        json_data = json.load(codecs.open(json_path, 'r', 'utf-8-sig'))
    except ValueError as err:
        return False
    return True, json_data


def start_validation(json_path):
    valid_json, tmp_data = validate_json(json_path)
    if valid_json:
        print("received valid json input")
        json_data = tmp_data
        return json_data
    else:
        print("given json is not valid")
