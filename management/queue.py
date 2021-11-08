from . import file_import


class QueueData:
    def __init__(self, model, title, valid, queue_position):
        self.model = model
        self.title = title
        self.valid = valid
        self.queue_position = queue_position

    def __lt__(self, other):
        return self.queue_position < other.queue_position


class QueueManager(object):
    def __init__(self, paths):
        self.paths = paths
        self.staged_files = None

        self.camera_queue_order = {
            "cameraPoseList": 0,
            "cameraProjection": 1,
            "screenPosData": 2,
            "anchorData": 3,
            "points": 4,
            "movie": 5
        }

        self.face_queue_order = {
            "facePoseList": 0,
            "meshGeometry": 1,
            "meshDataList": 2,
            "blendShapeData": 2
        }

        self.get_valid_files()

    def get_valid_files(self):
        for path in self.paths:
            self.process_data_for_queue(path)
        self.staged_files.sort()

    def process_data_for_queue(self, path):
        data = file_import.FileImporter(path)
        queue_position = self.get_queue_position(data.title)
        if queue_position != -1 and data.valid is True:
            data = QueueData(model=data.model_data, title=data.title, valid=data.valid, queue_position=queue_position)
            self.staged_files.append(data)

    def get_queue_position(self, title):
        cam_value = self.get_position(title, self.camera_queue_order)
        face_value = self.get_position(title, self.face_queue_order)

        if cam_value != -1:
            return cam_value
        elif face_value != -1:
            return face_value
        else:
            return -1

    @staticmethod
    def get_position(title, queue_type):
        for key in queue_type.keys():
            if title == key:
                value = queue_type[key]
                return value
        return -1

