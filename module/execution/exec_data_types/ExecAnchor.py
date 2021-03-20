from module.execution.objects import ReferenceObject
from module.execution.scene import Collections

from importlib import reload
reload(ReferenceObject)
reload(Collections)


def exec_anchor(model, name, col_name):
    reference_objects = []

    for data in model:
        m_obj = ReferenceObject.generate_empty_at(
            px=data.px, py=data.py, pz=data.pz, name=name, size=1)
        reference_objects.append(m_obj)

    Collections.add_list_to_collection(reference_objects, col_name)

