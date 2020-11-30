from .models.helper import AddSceneReference, BlendShapeMapping
import importlib
importlib.reload(AddSceneReference)
importlib.reload(BlendShapeMapping)


def none():
    print("none")


def exec_pose_data(model):
    active_scene = AddSceneReference.add_scene_properties(model)
    target_objects = AddSceneReference.get_selected_objects(1)

    for data in model:
        data.init_frame(active_scene)
        for m_object in target_objects:
            data.key_rot(m_object)
            data.key_pos(m_object)


def exec_face_mesh(model):
    active_scene = AddSceneReference.add_scene_properties(model)
    m_vertices = AddSceneReference.generate_empties((len(model[0].vertices)), size=0.01)

    for data in model:
        data.init_frame(active_scene)
        data.key_pos(m_vertices)


def exec_shape_keys(model):
    active_scene = AddSceneReference.add_scene_properties(model)
    objects = AddSceneReference.get_selected_objects(1)

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
    for point in model:
        point.create_point()


def exec_intrinsics_data(model):
    # get scene reference and ref to cam
    active_scene = AddSceneReference.add_scene_properties(model.camera_intrinsics)
    camera = AddSceneReference.get_scene_camera()

    # set scene res and get sensor dimensions
    model.set_scene_resolution(active_scene)
    sensor_width, sensor_height, scale, pixel_aspect_ratio = model.set_sensor_size_in_mm(
        'VERTICAL', active_scene, camera
    )
    # set camera focal length and lens shift
    model.set_focal_length(sensor_width, 24.0, active_scene, camera)
    print(sensor_width, sensor_height, scale, pixel_aspect_ratio)
    model.set_lens_shift(scale, active_scene, camera)

