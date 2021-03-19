from module.execution.objects import KeyframeAssistent
from module.execution.scene import Scene
from module.execution.exec_data_types import \
    ExecFacePose, ExecPose, ExecFaceAnim, ExecFaceGeometry, ExecPointCloud, \
    ExecShapeKeys, ExecMovie, ExecProjData, ExecScreenPos, ExecAnchor

import importlib

importlib.import_module('module.execution.models')
importlib.import_module('module.data_models.helper')
importlib.import_module('module.data_models.data')


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


def reset_timeline():
    scene = Scene.get_scene_context()
    KeyframeAssistent.init_keyframe(frame=1, scene=scene)