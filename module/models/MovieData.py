import bpy


class MovieData:
    def __init__(self, data_path):
        self.path = data_path

    def set_camera_movie(self, camera):
        movie = bpy.data.movieclips.load(self.path)
        camera.data.show_background_images = True
        bg = camera.data.background_images.new()
        bg.source = 'MOVIE_CLIP'
        bg.clip = movie

    def print_contents(self):
        print("path to .mov:", self.path)


def init_movie_data(path):
    print("init movie data", path)
    movie_model = MovieData(path)
    return movie_model
