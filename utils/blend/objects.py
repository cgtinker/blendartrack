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


def deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)


def select_object(obj):
    bpy.context.view_layer.objects.active = obj


def get_object(name):
    return bpy.data.objects[name]