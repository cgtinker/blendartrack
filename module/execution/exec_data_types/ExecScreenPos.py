from module.execution.processing.objects import ReferenceObject
from module.execution.processing.scene import Scene


def exec_screen_pos(batch, model):
    active_scene, camera = init_screen_to_world_data(model, batch)
    model.anchor_screen_pos_to_camera(scene=active_scene, camera=camera)


def init_screen_to_world_data(model, batch):
    active_scene = Scene.set_scene_frame_end(model.screen_to_world)
    if batch:
        camera = ReferenceObject.get_camera_by_name(name="Retargeted_Camera")
    else:
        camera = ReferenceObject.get_selected_camera()
    return active_scene, camera