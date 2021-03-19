from module.execution.processing.objects import KeyframeAssistent
from module.preperation.importing import DecodeJson
from module.execution.processing.objects import ReferenceObject
import importlib

importlib.reload(KeyframeAssistent)
importlib.reload(DecodeJson)
importlib.reload(ReferenceObject)


class Point:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def create_point(self, name, size):
        ReferenceObject.generate_empty_at(px=self.px, py=self.py, pz=self.pz, name=name, size=size)

    def print_contents(self):
        print("point cloud data:", self.px, self.py, self.pz)


def init_point_cloud(json_data, title):
    # array to store pose data
    point_cloud_model = []
    # decoding json
    for data in json_data[title]:
        px, py, pz = DecodeJson.get_vert_data(data)
        point = Point(px, py, pz)
        point_cloud_model.append(point)

    return point_cloud_model
