from module.execution.objects import KeyframeAssistent, Name
from module.execution.scene import Scene
from module.execution.exec_data_types import \
    ExecFacePose, ExecPose, ExecFaceAnim, ExecFaceGeometry, ExecPointCloud, \
    ExecShapeKeys, ExecMovie, ExecProjData, ExecScreenPos, ExecAnchor

import importlib

importlib.reload(ExecFacePose)
importlib.reload(ExecPose)
importlib.reload(ExecFaceAnim)
importlib.reload(ExecFaceGeometry)
importlib.reload(ExecPointCloud)
importlib.reload(ExecShapeKeys)
importlib.reload(ExecMovie)
importlib.reload(ExecProjData)
importlib.reload(ExecScreenPos)
importlib.reload(ExecAnchor)
importlib.reload(Scene)
importlib.reload(KeyframeAssistent)
importlib.reload(Name)

camera_name = "AR_Camera_"
face_name = "AR_Face_"


def reference_name(name):
    named_objects = Name.get_objects_with_name(name)
    return named_objects


def get_active_ar_camera_name():
    m_objects = reference_name(camera_name)
    m_name = str(camera_name + str(len(m_objects) - 1))
    return m_name


def none():
    print("none")


def exec_face_pose_data(model, batch):
    ExecFacePose.exec_face_pose(batch, model)


def exec_mesh_geometry(model, batch):
    ExecFaceGeometry.exec_face_geometry(batch, model)


def exec_face_mesh(model, batch):
    ExecFaceAnim.exec_face_anim(batch, model)


def exec_shape_keys(model, batch):
    ExecShapeKeys.exec_keys(batch, model)


def exec_pose_data(model, batch):
    m_objects = reference_name(camera_name)
    m_name = camera_name + str(len(m_objects))
    ExecPose.exec_pose(model, batch, m_name)


def exec_point_cloud_data(model, batch):
    ExecPointCloud.exec_point(model)


def exec_anchor_data(model, batch):
    ExecAnchor.exec_anchor(model)


def exec_movie_data(model, batch):
    m_name = get_active_ar_camera_name()
    ExecMovie.exec_mov(model, batch, m_name)


def exec_projection_data(model, batch):
    m_name = get_active_ar_camera_name()
    ExecProjData.exec_proj(model, batch, m_name)


def exec_screen_to_world_data(model, batch):
    m_name = get_active_ar_camera_name()
    ExecScreenPos.exec_screen_pos(model, batch, m_name)


def reset_timeline():
    scene = Scene.get_scene_context()
    KeyframeAssistent.init_keyframe(frame=1, scene=scene)
