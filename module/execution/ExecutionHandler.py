from module.execution.objects import KeyframeAssistent
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


def none():
    print("none")


def exec_pose_data(model, batch):
    ExecPose.exec_pose(batch, model)


def exec_face_pose_data(model, batch):
    ExecFacePose.exec_face_pose(batch, model)


def exec_mesh_geometry(model, batch):
    ExecFaceGeometry.exec_face_geometry(batch, model)


def exec_face_mesh(model, batch):
    ExecFaceAnim.exec_face_anim(batch, model)


def exec_shape_keys(model, batch):
    ExecShapeKeys.exec_keys(batch, model)


def exec_point_cloud_data(model, batch):
    ExecPointCloud.exec_point(model)


def exec_anchor_data(model, batch):
    ExecAnchor.exec_anchor(model)


def exec_movie_data(model, batch):
    ExecMovie.exec_mov(batch, model)


def exec_projection_data(model, batch):
    ExecProjData.exec_proj(batch, model)


def exec_screen_to_world_data(model, batch):
    ExecScreenPos.exec_screen_pos(batch, model)
    print("")
    print("?")
    print("processing and linking screen pos data")


def reset_timeline():
    scene = Scene.get_scene_context()
    KeyframeAssistent.init_keyframe(frame=1, scene=scene)