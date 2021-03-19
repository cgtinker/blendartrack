from module.execution.objects import ReferenceObject


def exec_anchor(model):
    for data in model:
        ReferenceObject.generate_empty_at(
            px=data.px, py=data.py, pz=data.pz, name="reference", size=1)
