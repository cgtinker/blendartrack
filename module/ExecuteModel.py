from .models.helper import BlendShapeMapping
from .models.data import ReferenceObject, Constraints, Scene
import importlib
importlib.reload(ReferenceObject)
importlib.reload(BlendShapeMapping)
importlib.reload(Constraints)
importlib.reload(Scene)


def none():
    print("none")


def exec_pose_data(model, batch):
    m_object, active_scene = init_pose_data(model, batch)
    parent = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, name="camera_parent", size=1)

    for data in model:
        data.init_frame(active_scene)
        data.key_pos(parent)
        data.key_rot(obj=parent, x_offset=90)

    Constraints.add_copy_location_constraint(obj=m_object, target_obj=parent, use_offset=False)
    Constraints.add_copy_rotation_constraint(obj=m_object, target_obj=parent, invert_y=True)


def init_pose_data(model, batch):
    active_scene = ReferenceObject.add_scene_properties(model)

    if batch:
        camera = ReferenceObject.create_new_camera(name="Retargeted_Camera")
        return camera, active_scene
    else:
        if ReferenceObject.object_selected():
            m_object = ReferenceObject.get_selected_object()
            return m_object, active_scene
        else:
            m_object = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, size=1)
            return m_object, active_scene


def exec_face_pose_data(model, batch):
    m_object, active_scene = init_face_pose_data(model, batch)

    for data in model:
        data.init_frame(active_scene)
        data.key_pos(m_object)
        data.key_rot(obj=m_object, x_offset=0)


def init_face_pose_data(model, batch):
    active_scene = ReferenceObject.add_scene_properties(model)

    if batch:
        m_object = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, name="Retarget_Face_Pos", size=1)
        return m_object, active_scene
    else:
        if ReferenceObject.object_selected():
            m_object = ReferenceObject.get_selected_object()
            return m_object, active_scene
        else:
            m_object = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, name="Retarget_Face_Pos", size=1)
            return m_object, active_scene


def exec_face_mesh(model, batch):
    active_scene, parent = init_face_mesh(model, batch)
    m_vertices = ReferenceObject.generate_empties((len(model[0].vertices)), size=0.01)
    print("importing face mesh model")

    for data in model:
        data.init_frame(active_scene)
        data.key_pos(m_vertices)

    for m_vert in m_vertices:
        m_vert.parent = parent

    Scene.disable_relation_lines()


def init_face_mesh(model, batch):
    active_scene = ReferenceObject.add_scene_properties(model)

    if batch:
        parent = ReferenceObject.get_object_by_name(name="Retarget_Face_Pos")
    else:
        parent = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, size=1, name="Face_Parent")

    return active_scene, parent


def exec_shape_keys(model, batch):
    if batch:
        print("hi")
    else:
        active_scene = ReferenceObject.add_scene_properties(model)
        objects = ReferenceObject.get_selected_objects(1)
        print("importing blend shape model")

        if len(objects) == 1:
            obj = objects[0]    # currently only enabling import for one selected obj
            keys = ReferenceObject.get_obj_blend_shape_ref(obj)   # getting stored blend shapes
            ref_dict = BlendShapeMapping.create_blend_shape_mapping(keys)    # reference for shape key import

            for data in model:
                data.init_frame(active_scene)
                data.keyframe_shape_keys(obj, ref_dict)
        else:
            print('more than one or no object selected')


def exec_point_cloud_data(model, batch):
    for point in model:
        point.create_point(name="point", size=0.01)


def exec_anchor_data(model, batch):
    for point in model:
        point.create_point(name="reference", size=1)


def exec_projection_data(model, batch):
    camera, aspect, fit, active_scene = init_projection_data(model, batch)
    sensor_width = camera.data.sensor_width
    model.set_camera_projection(sensor_width=sensor_width, aspect=aspect, fit=fit,
                                camera=camera, scene=active_scene)


def init_projection_data(model, batch):
    # get scene reference and ref to cam
    active_scene = ReferenceObject.add_scene_properties(model.camera_projection)
    # set scene resolution
    model.set_scene_resolution(active_scene)

    # get aspect ratio & sensor width
    aspect, fit = model.get_screen_aspect_ratio()

    if batch:
        camera = ReferenceObject.get_camera_by_name(name="Retargeted_Camera")
    else:
        camera = ReferenceObject.get_selected_camera()

    return camera, aspect, fit, active_scene


def exec_screen_to_world_data(model, batch):
    active_scene, camera = init_screen_to_world_data(model, batch)
    model.anchor_screen_pos_to_camera(scene=active_scene, camera=camera)


def init_screen_to_world_data(model, batch):
    active_scene = ReferenceObject.add_scene_properties(model.screen_to_world)
    if batch:
        camera = ReferenceObject.get_camera_by_name(name="Retargeted_Camera")
    else:
        camera = ReferenceObject.get_selected_camera()
    return active_scene, camera
