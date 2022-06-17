import src.utils.blend.objects
from ...utils.blend import collection
from ...utils.blend import reference
from ...utils import reference_names
from .. import iCustomData
from . import point


class PointCloud(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.title = title
        self.batch = batch

        self.model = None
        self.points = []

        self.collection = reference_names.pc_col
        self.name = reference_names.ar_point_cloud

    def initialize(self):
        self.model = point.initialize(self.json_data, self.title)

    def generate(self):
        for data in self.model:
            m_obj = src.utils.blend.objects.generate_empty_at(
                px=data.px, py=data.py, pz=data.pz, name=self.name, size=0.01)
            self.points.append(m_obj)

    def animate(self):
        pass

    def structure(self):
        collection.add_list_to_collection(self.points, self.collection)
