from module.execution.objects import ReferenceObject
from module.execution.scene import Collections

from importlib import reload
reload(ReferenceObject)
reload(Collections)


def exec_point(model, batch, name, col_name):
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

