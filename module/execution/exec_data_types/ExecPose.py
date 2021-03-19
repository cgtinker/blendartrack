from module.execution.objects import ReferenceObject, Constraints, KeyframeAssistent
from module.execution.scene import Scene


def exec_pose(model, batch, name):
    m_object, active_scene = init_pose_data(model, batch, name)
    parent = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, name="camera_parent", size=1)

    for data in model:
        KeyframeAssistent.init_keyframe(data.frame, active_scene)
        KeyframeAssistent.set_pos_keyframe(data.px, data.py, data.pz, parent)
        KeyframeAssistent.set_rot_keyframe(data.rx + 90, data.ry, data.rz, parent)

    Constraints.add_copy_location_constraint(obj=m_object, target_obj=parent, use_offset=False)
    Constraints.add_copy_rotation_constraint(obj=m_object, target_obj=parent, invert_y=True)


def init_pose_data(model, batch, name):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        camera = get_camera(name)
        return camera, active_scene

    else:
        m_object, available = get_selected()

        if available:
            return m_object, active_scene
        else:
            m_object = create_empty(name)
            return m_object, active_scene


def get_camera(name):
    camera = ReferenceObject.create_new_camera(name)
    return camera


def get_selected():
    if ReferenceObject.is_object_selected():
        m_object = ReferenceObject.get_selected_object()
        return m_object, True
    return "", False


def create_empty(name):
    m_object = ReferenceObject.generate_empty_at((0, 0, 0, 1, name))
    return m_object
