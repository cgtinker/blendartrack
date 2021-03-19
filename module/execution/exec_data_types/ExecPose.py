from module.execution.processing.objects import ReferenceObject, Constraints
from module.execution.processing.scene import Scene


def init_pose_data(model, batch):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        camera = ReferenceObject.create_new_camera(name="Retargeted_Camera")
        return camera, active_scene
    else:
        if ReferenceObject.is_object_selected():
            m_object = ReferenceObject.get_selected_object()
            return m_object, active_scene
        else:
            m_object = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, size=1, name="CameraMotion")
            return m_object, active_scene


def exec_pose(batch, model):
    m_object, active_scene = init_pose_data(model, batch)
    parent = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, name="camera_parent", size=1)
    for data in model:
        data.init_frame(active_scene)
        data.key_pos(parent)
        data.key_rot(obj=parent, x_offset=90)
    Constraints.add_copy_location_constraint(obj=m_object, target_obj=parent, use_offset=False)
    Constraints.add_copy_rotation_constraint(obj=m_object, target_obj=parent, invert_y=True)
