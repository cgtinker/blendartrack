from ..objects import ReferenceObject
from ..scene import Collections
import bpy
from importlib import reload
reload(ReferenceObject)
reload(Collections)


def exec_point(model, batch, name, col_name):
    get_user_input = bpy.context.scene.m_cgtinker_blendartrack

    if get_user_input.bool_point_cloud:
        import_point_cloud(model, col_name, name)


def import_point_cloud(model, col_name, name):
    reference_objects = []

    for data in model:
        m_obj = ReferenceObject.generate_empty_at(
            px=data.px, py=data.py, pz=data.pz, name=name, size=0.01)
        reference_objects.append(m_obj)

    if Collections.collection_exists(col_name):
        for obj in reference_objects:
            Collections.add_obj_to_collection(col_name, obj)

    else:
        Collections.create_collection(col_name, True)
        for obj in reference_objects:
            Collections.add_obj_to_collection(col_name, obj)
