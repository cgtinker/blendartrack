from module.execution.objects import ReferenceObject
from module.execution.scene import Scene


def exec_proj(batch, model):
    camera, aspect, fit, active_scene = init_projection_data(model, batch)
    sensor_width = camera.data.sensor_width
    model.set_camera_projection(sensor_width=sensor_width, aspect=aspect, fit=fit,
                                camera=camera, scene=active_scene)


def init_projection_data(model, batch):
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
        camera = ReferenceObject.get_camera_by_name(name="Retargeted_Camera")
    else:
        camera = ReferenceObject.get_selected_camera()

    return camera, aspect, fit, active_scene
