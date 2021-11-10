from import_models.reference import anchors, point_cloud
from import_models.face import face_parent_animation, face_mesh, face_empties_animation, face_mesh_animation
from import_models.camera import camera_lens_shift, camera_parent_animation, camera_projection, movie
from utils.blend import scene, keyframe

import importlib
importlib.reload(face_parent_animation)
importlib.reload(face_mesh)
importlib.reload(face_mesh_animation)
importlib.reload(face_empties_animation)
importlib.reload(camera_projection)
importlib.reload(anchors)
importlib.reload(face_mesh)
importlib.reload(movie)
importlib.reload(camera_lens_shift)
importlib.reload(camera_parent_animation)


class ExecutionManager(object):
    def __init__(self, staged_files):
        self.staged_files = staged_files
        self.available_models = {
            "facePoseList": face_parent_animation.AnimatedFaceParent,
            "meshDataList": face_mesh_animation.FaceMeshAnimation,
            # "meshDataList": face_empties_animation.AnimatedFaceEmpties,
            "meshGeometry": face_mesh.FaceMesh,
            "blendShapeData": "blend shapes",

            "cameraPoseList": camera_parent_animation.CameraParent,
            "cameraProjection": camera_projection.CameraProjection,
            "screenPosData": camera_lens_shift.CameraLensShift,

            "anchorData": anchors.Anchors,
            "points": point_cloud.PointCloud,
            "movie": movie.Movie
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
                model = self.model(json_data=file.json_data, batch=True, title=self.model_title)
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
