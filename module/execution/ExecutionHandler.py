from .objects import KeyframeAssistent, Name
from .scene import Scene
from .exec_data_types import ExecFacePose, ExecPose, ExecFaceAnim, ExecFaceGeometry, ExecPointCloud, ExecShapeKeys, \
    ExecMovie, ExecProjData, ExecScreenPos, ExecAnchor

import importlib
import bpy

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

ar_camera = "AR_Camera_"
camera_parent = "Camera_Motion_"
cam_col = "Camera"

ar_face = "AR_Face_"
face_parent = "Face_Motion_"
face_col = "Face"
face_empty_col = "Face_Empties"

ar_reference = "AR_Reference_"
ref_col = "Reference"

ar_point_cloud = "AR_Point_"
pc_col = "Cloud"


def none():
    print("none")


def exec_face_pose_data(model, batch):
    print("exec_face_pose_data")
    m_name = Name.set_reference_name(face_parent)
    ExecFacePose.exec_face_pose(model, batch, m_name, face_col)


def exec_mesh_geometry(model, batch):
    get_user_input = bpy.context.scene.m_cgtinker_blendartrack
    print("exec_mesh_geometry")
    if get_user_input.enum_face_type == 'MESH':
        m_name = Name.set_reference_name(ar_face)
        parent_name = Name.get_active_reference(face_parent)
        ExecFaceGeometry.exec_face_geometry(model, batch, m_name, parent_name, face_col)


def exec_face_anim(model, batch):
    get_user_input = bpy.context.scene.m_cgtinker_blendartrack
    print("exec_face_anim")
    if get_user_input.enum_face_type == 'MESH':
        m_name = Name.get_active_reference(ar_face)
        parent_name = Name.get_active_reference(face_parent)
        ExecFaceAnim.exec_face_anim(model, batch, m_name, parent_name, "")
    else:
        m_name = Name.get_active_reference(face_parent)
        parent_name = Name.get_active_reference(face_parent)
        ExecFaceAnim.exec_face_anim(model, batch, m_name, parent_name, face_empty_col)


# TODO: Implement shape key logic for iOS
def exec_shape_keys(model, batch):
    ExecShapeKeys.exec_keys(batch, model)


def exec_pose_data(model, batch):
    print("exec_pose_data")
    m_name = Name.set_reference_name(ar_camera)
    parent_name = Name.set_reference_name(camera_parent)

    ExecPose.exec_pose(model, batch, m_name, parent_name, cam_col)


def exec_point_cloud_data(model, batch):
    print("exec_point_cloud_data")
    m_name = Name.set_reference_name(ar_point_cloud)
    ExecPointCloud.exec_point(model, batch, m_name, pc_col)


def exec_anchor_data(model, batch):
    print("exec_anchor_data")
    m_name = Name.set_reference_name(ar_reference)
    ExecAnchor.exec_anchor(model, m_name, ref_col)


def exec_movie_data(model, batch):
    print("exec_movie_data")
    m_name = Name.get_active_reference(ar_camera)
    ExecMovie.exec_mov(model, batch, m_name)


def exec_projection_data(model, batch):
    print("exec_projection_data")
    m_name = Name.get_active_reference(ar_camera)
    ExecProjData.exec_proj(model, batch, m_name)


def exec_screen_to_world_data(model, batch):
    print("exec_screen_to_world_data")
    m_name = Name.get_active_reference(ar_camera)
    ExecScreenPos.exec_screen_pos(model, batch, m_name)


def reset_timeline():
    print("reset_timeline")
    scene = Scene.get_scene_context()
    KeyframeAssistent.init_keyframe(frame=1, scene=scene)
