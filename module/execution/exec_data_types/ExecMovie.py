from module.execution.objects import ReferenceObject


def exec_mov(batch, model):
    if batch:
        camera = ReferenceObject.get_camera_by_name(name="Retargeted_Camera")
    else:
        camera = ReferenceObject.get_selected_camera()
    model.set_camera_movie(camera)