from module.execution.objects import ReferenceObject, KeyframeAssistent
from module.execution.scene import Scene


def exec_face_pose(batch, model):
    m_object, active_scene = init_face_pose_data(model, batch)
    for data in model:
        KeyframeAssistent.init_keyframe(data.frame, active_scene)
        KeyframeAssistent.set_pos_keyframe(data.px, data.py, data.pz, m_object)
        KeyframeAssistent.set_rot_keyframe(data.rx, data.ry, data.rz, m_object)

        # data.init_frame(active_scene)
        # data.key_pos(m_object)
        # data.key_rot(obj=m_object, x_offset=0)


def init_face_pose_data(model, batch):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        m_object = ReferenceObject.generate_empty_at(
            px=0, py=0, pz=0, name="Retarget_Face_Pos", size=1)
        return m_object, active_scene
    else:
        if ReferenceObject.is_object_selected():
            m_object = ReferenceObject.get_selected_object()
            return m_object, active_scene
        else:
            m_object = ReferenceObject.generate_empty_at(
                px=0, py=0, pz=0, name="Retarget_Face_Pos", size=1)
            return m_object, active_scene
