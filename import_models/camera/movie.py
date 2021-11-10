from utils.custom_data import iCustomData
from utils import reference_names
from utils.blend import reference, name
import bpy


class Movie(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.path = json_data
        self.title = title
        self.batch = batch

        self.model = None
        self.camera = None

        self.camera_name = reference_names.ar_camera

    def initialize(self):
        self.model = MovieData(self.path)

    def generate(self):
        if self.batch:
            self.camera = name.get_camera_by_name(self.camera_name)
        else:
            self.camera = reference.get_selected_camera()

        self.set_camera_movie()

    def animate(self):
        pass

    def structure(self):
        pass

    def set_camera_movie(self):
        # TODO: apply movie path in utils/blend
        movie = bpy.data.movieclips.load(self.path)
        self.camera.data.show_background_images = True
        bg = self.camera.data.background_images.new()
        bg.source = 'MOVIE_CLIP'
        bg.clip = movie


class MovieData:
    def __init__(self, data_path):
        self.path = data_path

    def print_contents(self):
        print("path to .mov:", self.path)

