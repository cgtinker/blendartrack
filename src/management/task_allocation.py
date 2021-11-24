from src.import_models.reference import anchors, point_cloud
from src.import_models.face import face_parent_animation, face_empties_animation
from src.import_models.face import face_mesh_animation, face_mesh
from src.import_models.camera import camera_lens_shift, camera_parent_animation, camera_projection, movie
from src.utils.blend import scene, keyframe
from src.utils.blend import user

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
importlib.reload(point_cloud)
importlib.reload(user)


class TaskAllocator(object):
    def __init__(self, staged_files):
        self.staged_files = staged_files

        self.mesh_bool = user.get_user().enum_face_type == 'MESH'
        self.available_models = {
            "facePoseList":     [face_parent_animation.AnimatedFaceParent, True],
            "meshGeometry":     [face_mesh.FaceMesh, self.mesh_bool],
            "meshDataList":     [self.set_face_animation_model(),           True],

            "cameraPoseList":   [camera_parent_animation.CameraParent, True],
            "cameraProjection": [camera_projection.CameraProjection, True],
            "screenPosData":    [camera_lens_shift.CameraLensShift, True],
            "anchorData":       [anchors.Anchors, user.get_user().bool_reference_point],
            "points":           [point_cloud.PointCloud, user.get_user().bool_point_cloud],
            "movie":            [movie.Movie, True]
        }

        self.not_implemented = {
            "blendShapeData": "blend shapes",
        }

        self.model = None
        self.model_title = ""
        self.staged_models = []

        self.initialize()

    def initialize(self):
        if len(self.staged_files) == 1:
            self.get_execution_model(self.staged_files[0])
            if self.model[1]:                           # if model to import
                model = self.model[0](json_data=self.staged_files[0].json_data, batch=False, title=self.model_title)
                self.staged_models.append(model)     # stage model

        elif len(self.staged_files) > 1:
            for file in self.staged_files:
                self.get_execution_model(file)
                if self.model[1]:                       # if model to import
                    model = self.model[0](json_data=file.json_data, batch=True, title=self.model_title)
                    self.staged_models.append(model) # stage model

        self.reset_timeline()

    def get_execution_model(self, file):
        user.get_user()
        for title in self.available_models:
            try:
                if title == file.title:
                    self.model = self.available_models[title]
                    self.model_title = title
            except KeyError:
                print("key error occurs on title: ", title)
                pass

    def set_face_animation_model(self):
        if self.mesh_bool:
            return face_mesh_animation.FaceMeshAnimation
        else:
            return face_empties_animation.AnimatedFaceEmpties

    # TODO: should be somewhere else (in blend scripts)
    @staticmethod
    def reset_timeline():
        print("reset_timeline")
        active_scene = scene.get_scene()
        keyframe.init_keyframe(frame=1, scene=active_scene)
