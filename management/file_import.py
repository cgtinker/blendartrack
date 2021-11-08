from ..utils import pathing, json_validator
from ..utils.custom_data import init_data_types


class FileImporter(object):
    def __init__(self, data_path):
        self.data_path = data_path
        self.json_data = None
        self.model_data = None
        self.title = None
        self.valid = False

        self.reference_methods = {
            "none": init_data_types.none,
            "cameraPoseList": init_data_types.init_pose_model,
            "facePoseList": init_data_types.init_pose_model,

            "meshDataList": init_data_types.init_face_mesh_model,
            "meshGeometry": init_data_types.init_face_mesh_geo_model,
            "blendShapeData": init_data_types.init_blend_shape_model,
            "cameraProjection": init_data_types.init_camera_projection_model,

            "points": init_data_types.init_point_cloud_model,
            "anchorData": init_data_types.init_point_cloud_model,

            "screenPosData": init_data_types.init_screen_to_world_model
        }

        self.receive_data_from_file()

    def receive_data_from_file(self):
        if pathing.is_json_path(self.data_path):
            self.import_json_data()

        elif pathing.is_movie_path(self.data_path):
            self.model_data, self.valid = init_data_types.init_movie_model(self.data_path)
            self.title = "movie"

        else:
            self.return_file_not_valid()

    def import_json_data(self):
        # validate the json file
        self.json_data, valid_contents, valid_type = self.validate_json_data()
        if valid_type is True and valid_contents is True:
            # get reference to import class type
            init_model, title = self.set_method_reference()
            if init_model != init_data_types.none:
                # finally import the data
                model_data, is_imported = init_model(self.json_data, title)
                self.model_data, self.title, self.valid = model_data, title, is_imported

            else:
                self.return_file_not_valid()

        else:
            self.return_file_not_valid()

    def validate_json_data(self):
        # validate json structure
        valid_type, json_data = json_validator.is_json_valid(self.data_path)
        valid_contents = json_validator.is_json_iterable(self.data_path)
        return json_data, valid_contents, valid_type

    def set_method_reference(self):
        init_model = init_data_types.none
        title = ""

        for json_title in self.reference_methods:
            if json_title in self.json_data:
                init_model = self.reference_methods[json_title]
                title = json_title

        return init_model, title

    def return_file_not_valid(self):
        print("Couldn't find a fitting import model")
        self.model_data, self.title, self.valid = [], "", False
