import bpy


def get_objects():
    objects = bpy.data.objects
    return objects


def is_camera(obj):
    if obj.type == "CAMERA":
        return True
    else:
        return False


def is_mesh(obj):
    if obj.type == "MESH":
        return True
    else:
        return False
