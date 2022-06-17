import json
import codecs


def is_json_valid(json_path):
    try:
        json_data = json.load(codecs.open(json_path, 'r', 'utf-8-sig'))
    except ValueError as err:
        print('json not valid: ', err, json_path)
        return False, ""

    return True, json_data


def is_json_iterable(contents):
    try:
        iter(contents)
    except TypeError:
        return False
    return True

