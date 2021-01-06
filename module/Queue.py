from . import ImportJson, ExecuteModel

import importlib
importlib.reload(ImportJson)
importlib.reload(ExecuteModel)


class QueueData:
    def __init__(self, model, title, valid, queue):
        self.model = model
        self.title = title
        self.valid = valid
        self.queue = queue

    def __lt__(self, other):
        return self.queue < other.queue

    def print_contents(self):
        print(self.title, "|| valid:", self.valid, "|| queue position:", self.queue)


# getting the queue position
def get_queue_position(title):
    cam_value = get_camera_queue_pos(title)
    face_value = get_face_queue_pos(title)

    if cam_value != -1:
        return cam_value
    elif face_value != -1:
        return face_value
    else:
        return -1


def get_camera_queue_pos(title):
    camera_queue = {
        "cameraPoseList": 0,
        "cameraProjection": 1,
        "screenPosData": 2,
        "anchorData": 3,
        "points": 4
    }

    for key in camera_queue.keys():
        if title == key:
            value = camera_queue[key]
            return value
    return -1


def get_face_queue_pos(title):
    face_queue = {
        "facePoseList": 0,
        "meshGeometry": 1,
        "meshDataList": 2,
        "blendShapeData": 2
    }

    for key in face_queue.keys():
        if title == key:
            value = face_queue[key]
            return value
    return -1


# queue the models
def queue_files(paths):
    models = []
    for path in paths:
        # import models
        model_data, title, valid = ImportJson.import_json_data(path)
        if valid:
            # add queue position
            queue = get_queue_position(title)
            if queue != -1:
                data = QueueData(model=model_data, title=title, valid=valid, queue=queue)
                models.append(data)
    
    # execution order prepared
    models.sort()
    # execution
    execute_queue(models)


# execute the models in queue
def execute_queue(models):
    exec_models = {
        "facePoseList": ExecuteModel.exec_face_pose_data,
        "meshDataList": ExecuteModel.exec_face_mesh,
        "blendShapeData": ExecuteModel.exec_shape_keys,
        "meshGeometry": ExecuteModel.exec_mesh_geometry,

        "cameraPoseList": ExecuteModel.exec_pose_data,
        "cameraProjection": ExecuteModel.exec_projection_data,
        "screenPosData": ExecuteModel.exec_screen_to_world_data,
        "anchorData": ExecuteModel.exec_anchor_data,

        "points": ExecuteModel.exec_point_cloud_data
    }

    if len(models) == 1:
        exec_model = get_exec_model(models[0], exec_models)
        exec_model(model=models[0].model, batch=False)

    elif len(models) > 1:
        for model in models:
            exec_model = get_exec_model(model, exec_models)
            exec_model(model=model.model, batch=True)


# get the execution model
def get_exec_model(model, exec_models):
    for title in exec_models:
        if title == model.title:
            exec_model = exec_models[title]
            return exec_model
