from src.utils.json import validator
from src.utils import pathing


class QueueData:
    def __init__(self, json_data, title, valid, queue_position):
        self.json_data = json_data
        self.title = title
        self.valid = valid
        self.queue_position = queue_position

    def __lt__(self, other):
        return self.queue_position < other.queue_position


class QueueManager(object):
    def __init__(self, paths):
        self.paths = paths
        self.staged_files = []
        # TODO: should depend on user input
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
            if pathing.is_json_path(path):
                json_data, valid_contents, valid_type = self.validate_json_data(path)
                if valid_type is True and valid_contents is True:
                    self.process_data_for_queue(json_data)
                else:
                    print("json data is not valid")
            elif pathing.is_movie_path(path):
                data = QueueData(json_data=path, title="movie", valid=True,
                                 queue_position=self.camera_queue_order["movie"])
                self.staged_files.append(data)

            else:
                print("given path is not valid")

        self.staged_files.sort()

    def process_data_for_queue(self, json_data):
        for key in {**self.camera_queue_order, **self.face_queue_order}:
            if key in json_data:
                title = key
                queue_position = self.get_queue_position(key)

                if queue_position != -1:
                    data = QueueData(json_data=json_data, title=title, valid=True,
                                     queue_position=queue_position)
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
    def validate_json_data(path):
        # validate json structure
        valid_type, json_data = validator.is_json_valid(path)
        valid_contents = validator.is_json_iterable(path)
        return json_data, valid_contents, valid_type

    @staticmethod
    def get_position(title, queue_type):
        for key in queue_type.keys():
            if title == key:
                value = queue_type[key]
                return value
        return -1

