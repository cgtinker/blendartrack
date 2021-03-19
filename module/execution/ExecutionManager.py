from module.execution import ExecutionHandler
import importlib

importlib.reload(ExecutionHandler)


def get_exec_model(model, exec_models):
    for title in exec_models:
        if title == model.title:
            exec_model = exec_models[title]
            return exec_model


def execute_queue(models):
    exec_models = {
        "facePoseList": ExecutionHandler.exec_face_pose_data,
        "meshDataList": ExecutionHandler.exec_face_mesh,
        "blendShapeData": ExecutionHandler.exec_shape_keys,
        "meshGeometry": ExecutionHandler.exec_mesh_geometry,

        "cameraPoseList": ExecutionHandler.exec_pose_data,
        "cameraProjection": ExecutionHandler.exec_projection_data,
        "screenPosData": ExecutionHandler.exec_screen_to_world_data,
        "anchorData": ExecutionHandler.exec_anchor_data,

        "points": ExecutionHandler.exec_point_cloud_data,

        "movie": ExecutionHandler.exec_movie_data
    }

    if len(models) == 1:
        exec_model = get_exec_model(models[0], exec_models)
        exec_model(model=models[0].model, batch=False)

    elif len(models) > 1:
        for model in models:
            exec_model = get_exec_model(model, exec_models)
            exec_model(model=model.model, batch=True)
    ExecutionHandler.reset_timeline()
