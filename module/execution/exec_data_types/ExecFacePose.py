from ..objects import ReferenceObject, KeyframeAssistent
from ..scene import Scene, Collections

from importlib import reload
reload(ReferenceObject)
reload(KeyframeAssistent)
reload(Scene)
reload(Collections)


def exec_face_pose(model, batch, name, col_name):
    m_object, active_scene = init_face_pose_data(model, batch, name)
    for data in model:
        KeyframeAssistent.init_keyframe(data.frame, active_scene)
        KeyframeAssistent.set_pos_keyframe(data.px, data.py, data.pz, m_object)
        KeyframeAssistent.set_rot_keyframe(data.rx, data.ry, data.rz, m_object)
    Collections.add_obj_to_collection(col_name, m_object)


def init_face_pose_data(model, batch, name):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        m_object = ReferenceObject.generate_empty_at(
            px=0, py=0, pz=0, name=name, size=1)
        return m_object, active_scene
    else:
        if ReferenceObject.is_object_selected():
            m_object = ReferenceObject.get_selected_object()
            return m_object, active_scene
        else:
            m_object = ReferenceObject.generate_empty_at(
                px=0, py=0, pz=0, name=name, size=1)
            return m_object, active_scene
