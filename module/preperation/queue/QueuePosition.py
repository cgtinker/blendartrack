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
        "points": 4,
        "movie": 5
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
