from utils.custom_data import iCustomData
from abc import ABC
from models import animated_camera_motion, animated_face_empties, animated_face_parent_motion, animated_face_mesh
from utils.blend import scene, keyframe

import importlib
importlib.reload(animated_face_parent_motion)


class ExecutionManager(object):
    def __init__(self, staged_files):
        self.staged_files = staged_files
        self.available_models = {
            "facePoseList": animated_face_parent_motion.AnimatedFaceParentMotion,
            "meshDataList": "",
            "blendShapeData": "blend shapes",
            "meshGeometry": "",

            "cameraPoseList": "camera motion",
            "cameraProjection": "projection matrix",
            "screenPosData": "lens shift",

            "anchorData": "anchors",
            "points": "point cloud",
            "movie": "movie"
        }
        self.model = None
        self.model_title = ""
        self.staged_models = []

        self.initialize()

    def initialize(self):
        if len(self.staged_files) == 1:
            self.get_execution_model(self.staged_files[0])
            model = self.model(json_data=self.staged_files[0].json_data, batch=False, title=self.model_title)
            self.staged_models.append(model)

        elif len(self.staged_files) > 1:
            for file in self.staged_files:
                self.get_execution_model(file)
                model = self.model(json_data=self.staged_files.json_data, batch=True, title=self.model_title)
                self.staged_models.append(model)

        self.reset_timeline()

    def get_execution_model(self, file):
        for title in self.available_models:
            if title == file.title:
                self.model = self.available_models[title]
                self.model_title = title

    # TODO: should be somewhere else (in blend scripts)
    @staticmethod
    def reset_timeline():
        print("reset_timeline")
        active_scene = scene.get_scene_context()
        keyframe.init_keyframe(frame=1, scene=active_scene)
