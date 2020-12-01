from .models.helper import AddSceneReference, BlendShapeMapping
import importlib
importlib.reload(AddSceneReference)
importlib.reload(BlendShapeMapping)


def none():
    print("none")


def exec_pose_data(model):
    active_scene = AddSceneReference.add_scene_properties(model)
    target_objects = AddSceneReference.get_selected_objects(1)
    print("importing camera pose model")
    for data in model:
        data.init_frame(active_scene)
        for m_object in target_objects:
            data.key_rot(m_object)
            data.key_pos(m_object)


def exec_face_mesh(model):
    active_scene = AddSceneReference.add_scene_properties(model)
    m_vertices = AddSceneReference.generate_empties((len(model[0].vertices)), size=0.01)
    print("importing face mesh model")
    for data in model:
        data.init_frame(active_scene)
        data.key_pos(m_vertices)


def exec_shape_keys(model):
    active_scene = AddSceneReference.add_scene_properties(model)
    objects = AddSceneReference.get_selected_objects(1)
    print("importing blend shape model")

    if len(objects) == 1:
        obj = objects[0]    # currently only enabling import for one selected obj
        keys = AddSceneReference.get_obj_blend_shape_ref(obj)   # getting stored blend shapes
        ref_dict = BlendShapeMapping.create_blend_shape_mapping(keys)    # reference for shape key import

        for data in model:
            data.init_frame(active_scene)
            data.keyframe_shape_keys(obj, ref_dict)
    else:
        print('more than one or no object selected')


def exec_point_cloud_data(model):
    print("importing point cloud model")

    for point in model:
        point.create_point()


def exec_projection_data(model):
    # get scene reference and ref to cam
    active_scene = AddSceneReference.add_scene_properties(model.camera_projection)
    camera = AddSceneReference.get_scene_camera()

    # set scene resolution
    model.set_scene_resolution(active_scene)

    # get aspect ratio & sensor width
    aspect, fit = model.get_screen_aspect_ratio()
    sensor_width = camera.data.sensor_width
    print("importing camera projection model")

    # setting camera specific data
    model.set_camera_projection(sensor_width=sensor_width, aspect=aspect, fit=fit,
                                camera=camera, scene=active_scene)

