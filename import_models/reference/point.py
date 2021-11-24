from utils.json import decoder


class Point:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def print_contents(self):
        print("point cloud data:", self.px, self.py, self.pz)


def initialize(json_data, title):
    # array to store pose data
    point_cloud_model = []
    # decoding json
    for data in json_data[title]:
        px, py, pz = decoder.get_vert_data(data)
        point = Point(px, py, pz)
        point_cloud_model.append(point)

    return point_cloud_model
