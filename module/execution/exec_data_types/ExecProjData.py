from module.execution.objects import ReferenceObject, KeyframeAssistent, Name
from module.execution.scene import Scene
from importlib import reload

reload(ReferenceObject)
reload(KeyframeAssistent)
reload(Scene)
reload(Name)


def exec_proj(model, batch, name):
    camera, aspect, fit, active_scene = init_projection_data(model, batch, name)
    sensor_width = camera.data.sensor_width
    projection_data = model.get_camera_projection_data()
    set_proj_data(projection_data, aspect, fit, sensor_width, active_scene, camera)
    # model.set_camera_projection(sensor_width=sensor_width, aspect=aspect, fit=fit, camera=camera, scene=active_scene)


def set_proj_data(projection_data, aspect, fit, sensor_width, scene, camera):
    for data in projection_data:
        focal_length, frame = data.get_focal_length(
            aspect=aspect, fit=fit, sensor_width=sensor_width
        )
        shift_x, shift_y = data.get_lens_shift(aspect=aspect, fit=fit)
        KeyframeAssistent.init_keyframe(scene=scene, frame=frame)
        print("retargeting camera projection data at frame ", frame, end='\r')
        KeyframeAssistent.set_camera_focal_length(focal_length=focal_length, camera=camera)
        KeyframeAssistent.set_camera_lens_shift(shift_x=shift_x, shift_y=shift_y, camera=camera)


def init_projection_data(model, batch, name):
    # get scene reference and ref to cam
    active_scene = Scene.set_scene_frame_end(model.camera_projection)
    # set scene resolution
    Scene.set_scene_resolution(
        active_scene,
        model.resolution.screen_width,
        model.resolution.screen_height)
    # get aspect ratio & sensor width
    aspect, fit = model.get_screen_aspect_ratio()
    if batch:
        camera = Name.get_camera_by_name(name)
    else:
        camera = ReferenceObject.get_selected_camera()

    return camera, aspect, fit, active_scene
