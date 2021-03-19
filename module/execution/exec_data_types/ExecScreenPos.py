from module.execution.objects import ReferenceObject, KeyframeAssistent
from module.execution.scene import Scene
from module.mapping import WorldToCameraScreen


def exec_screen_pos(batch, model):
    active_scene, camera = init_screen_to_world_data(model, batch)
    screen_pos_data = model.get_screen_pos_data()
    for data in screen_pos_data:
        set_lens_shift(data, active_scene, camera)


def set_lens_shift(data, scene, camera):
    KeyframeAssistent.init_keyframe(frame=data.frame, scene=scene)
    if data.z > 0:
        shift_x, shift_y = WorldToCameraScreen.world_to_camera_screen_space(
            scene=scene, camera=camera, px=data.tx, py=data.ty, pz=data.tz,
            aim_x=data.x, aim_y=data.y
        )
        KeyframeAssistent.set_camera_lens_shift(shift_x=shift_x, shift_y=shift_y, camera=camera)


def init_screen_to_world_data(model, batch):
    active_scene = Scene.set_scene_frame_end(model.screen_to_world)
    if batch:
        camera = ReferenceObject.get_camera_by_name(name="Retargeted_Camera")
    else:
        camera = ReferenceObject.get_selected_camera()
    return active_scene, camera
