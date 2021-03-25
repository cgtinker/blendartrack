from ..objects import ReferenceObject, Name
import bpy

from importlib import reload
reload(Name)
reload(ReferenceObject)


def exec_mov(model, batch, name):
    if batch:
        camera = Name.get_camera_by_name(name)
    else:
        camera = ReferenceObject.get_selected_camera()

    path = model.path
    set_camera_movie(path, camera)


def set_camera_movie(path, camera):
    movie = bpy.data.movieclips.load(path)
    camera.data.show_background_images = True
    bg = camera.data.background_images.new()
    bg.source = 'MOVIE_CLIP'
    bg.clip = movie
