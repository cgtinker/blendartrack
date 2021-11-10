from . import ExecutionHandler
import importlib

importlib.reload(ExecutionHandler)


class ExecutionManager(object):
    def __init__(self, models):
        self.models = models
        self.exec_models = {
            "facePoseList": ExecutionHandler.exec_face_pose_data,
            "meshDataList": ExecutionHandler.exec_face_anim,
            "blendShapeData": ExecutionHandler.exec_shape_keys,
            "meshGeometry": ExecutionHandler.exec_mesh_geometry,

            "cameraPoseList": ExecutionHandler.exec_pose_data,
            "cameraProjection": ExecutionHandler.exec_projection_data,
            "screenPosData": ExecutionHandler.exec_screen_to_world_data,
            "anchorData": ExecutionHandler.exec_anchor_data,

            "points": ExecutionHandler.exec_point_cloud_data,

            "movie": ExecutionHandler.exec_movie_data
        }

        self.exec_model = None

    def execute_queue(self):
        if len(self.models) == 1:
            self.get_execution_type(self.models[0])
            self.exec_model(model=self.models[0].model, batch=False)

        elif len(self.models) > 1:
            for model in self.models:
                self.get_execution_type(model)
                self.exec_model(model=model.model, batch=True)

        ExecutionHandler.reset_timeline()

    def get_execution_type(self, model):
        for title in self.exec_models:
            if title == model.batch:
                self.exec_model = self.exec_models[title]


"""
def get_exec_model(model, exec_models):
    for title in exec_models:
        if title == model.title:
            exec_model = exec_models[title]
            return exec_model


def execute_queue(import_models):
    exec_models = {
        "facePoseList": ExecutionHandler.exec_face_pose_data,
        "meshDataList": ExecutionHandler.exec_face_anim,
        "blendShapeData": ExecutionHandler.exec_shape_keys,
        "meshGeometry": ExecutionHandler.exec_mesh_geometry,

        "cameraPoseList": ExecutionHandler.exec_pose_data,
        "cameraProjection": ExecutionHandler.exec_projection_data,
        "screenPosData": ExecutionHandler.exec_screen_to_world_data,
        "anchorData": ExecutionHandler.exec_anchor_data,

        "points": ExecutionHandler.exec_point_cloud_data,

        "movie": ExecutionHandler.exec_movie_data
    }

    if len(import_models) == 1:
        exec_model = get_exec_model(import_models[0], exec_models)
        exec_model(model=import_models[0].model, batch=False)

    elif len(import_models) > 1:
        for model in import_models:
            exec_model = get_exec_model(model, exec_models)
            exec_model(model=model.model, batch=True)
    ExecutionHandler.reset_timeline()
"""