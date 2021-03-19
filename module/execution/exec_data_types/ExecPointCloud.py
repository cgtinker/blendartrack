from module.execution.objects import ReferenceObject


def exec_point(model):
    for data in model:
        ReferenceObject.generate_empty_at(
            px=data.px, py=data.py, pz=data.pz, name="point_cloud", size=0.01)
