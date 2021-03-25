from ..objects import ReferenceObject, KeyframeAssistent, Name
from ..scene import Scene
from ...mapping import WorldToCameraScreen
from importlib import reload

reload(WorldToCameraScreen)


def exec_screen_pos(model, batch, name):
    active_scene, camera = init_screen_to_world_data(model, batch, name)
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


def init_screen_to_world_data(model, batch, name):
    screen_pos_data = model.get_screen_pos_data()
    active_scene = Scene.set_scene_frame_end(screen_pos_data)
    if batch:
        camera = Name.get_camera_by_name(name)
    else:
        camera = ReferenceObject.get_selected_camera()
    return active_scene, camera
