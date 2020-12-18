import json
import codecs


# validation of the incoming json
def validate_json(json_path):
    try:
        json_data = json.load(codecs.open(json_path, 'r', 'utf-8-sig'))
    except ValueError as err:
        print('json not valid: ', err)
        return False, ""

    return True, json_data
