from mathutils import Vector


def is_int(val):
    valid = isinstance(val, int)
    return valid


def is_float(val):
    valid = isinstance(val, float)
    return valid


def is_list(val):
    valid = isinstance(val, list)
    return valid


def is_vector(val):
    valid = isinstance(val, Vector)
    return valid
