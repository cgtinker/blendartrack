import src.utils.blend.objects
from .. import iCustomData
from ...utils import reference_names
from ...utils.blend import name
from ...utils.blend import reference
import bpy


class Movie(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.path = json_data
        self.title = title
        self.batch = batch

        self.model = None
        self.camera = None

        self.name = src.utils.blend.objects.get_active_reference(reference_names.ar_camera)

    def initialize(self):
        self.model = MovieData(self.path)

    def generate(self):
        if self.batch:
            self.camera = src.utils.blend.objects.get_camera_by_name(self.name)
        else:
            self.camera = src.utils.blend.objects.get_selected_camera()

        self.set_camera_movie()

    def animate(self):
        pass

    def structure(self):
        pass

    def set_camera_movie(self):
        # TODO: apply movie path in utils/blend
        movie = bpy.data.movieclips.load(self.path)
        src.utils.blend.objects.data.show_background_images = True
        bg = src.utils.blend.objects.data.background_images.new()
        bg.source = 'MOVIE_CLIP'
        bg.clip = movie


class MovieData:
    def __init__(self, data_path):
        self.path = data_path

    def __repr__(self):
        return f'path to .mov: {self.path}'

