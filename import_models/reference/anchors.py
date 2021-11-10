from utils.custom_data import iCustomData
from utils.blend import reference, collection
from utils import reference_names
from import_models import point


class Anchors(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.title = title
        self.batch = batch

        self.model = None
        self.anchors = []

        self.collection = reference_names.ref_col
        self.name = reference_names.ar_reference

    def initialize(self):
        self.model = point.initialize(self.json_data, self.title)

    def generate(self):
        for data in self.model:
            m_obj = reference.generate_empty_at(
                px=data.px, py=data.py, pz=data.pz, name=self.name, size=1)
            self.anchors.append(m_obj)

    def animate(self):
        pass

    def structure(self):
        collection.add_list_to_collection(self.anchors, self.collection)

