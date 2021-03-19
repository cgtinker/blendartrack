import bpy
from module.execution.objects import ReferenceObject


def get_objects_with_name(name):
    objects = bpy.data.objects
    object_names = []

    for o in objects:
        object_names.append(o.name)

    objects_with_name = []
    for n in object_names:
        if name in n:
            objects_with_name.append(name)

    return objects_with_name


def get_object_by_name(name):
    m_object = bpy.data.objects.get(name)
    if m_object:
        return m_object
    else:
        m_object = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, size=1, name="empty")
        return m_object


def get_camera_by_name(name):
    camera = bpy.data.objects.get(name)
    if camera:
        return camera
    else:
        camera = ReferenceObject.create_new_camera(name)
        return camera


def is_name_available(name):
    ref_name = bpy.data.objects.get(name)
    if ref_name:
        return True
    else:
        return False
