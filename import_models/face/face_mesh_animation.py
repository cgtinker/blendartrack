from import_models import iCustomData
from utils.blend import name
from utils.mapping import VertexAnimation
from import_models.face import face_anim_data
from utils import reference_names

import importlib
importlib.reload(VertexAnimation)


class FaceMeshAnimation(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.title = title
        self.batch = batch

        self.ar_face = reference_names.ar_face
        self.collection = reference_names.face_col
        self.parent = reference_names.face_parent

        self.exec_type = None
        self.model = []

        self.face_mesh = None
        self.face_parent = None

    def initialize(self):
        self.model = face_anim_data.initialize(self.json_data, self.title)

    def generate(self):
        face_reference = name.get_active_reference(self.ar_face)
        self.face_mesh = name.get_object_by_name(face_reference)
        self.face_parent = name.get_active_reference(self.parent)

    def animate(self):
        frames = [data.frame for data in self.model]
        positions = [data.get_positions() for data in self.model]
        VertexAnimation.animate_geometry(self.face_mesh, frames, self.model)

    def structure(self):
        pass
