from .helper import KeyframeAssistent, JsonDecoder, Mesher

import importlib
importlib.reload(KeyframeAssistent)
importlib.reload(JsonDecoder)
importlib.reload(Mesher)


class MeshGeometry:
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices

    def get_vertices(self):
        m_vertices = []
        for i in range(len(self.vertices)):
            m_vertex = self.vertices[i].get_vertex()
            m_vertices.append(m_vertex)
        return m_vertices

    def get_faces(self):
        faces = (list(self.chunks(self.indices, 3)))
        return faces

    @staticmethod
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def print_contents(self):
        for index in self.indices:
            print(index)
        for mesh_vertex in self.vertices:
            mesh_vertex.print_vert_content()


class Vertex:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def get_vertex(self):
        m_vertex = (self.px, self.py, self.pz)
        return m_vertex

    def print_vert_content(self):
        print('vert: px', self.px, 'vert: py', self.py, 'vert: pz', self.pz)


def init_mesh_geo_model(json_data, title):
    # decoding json
    vertices = []
    for i in range(len(json_data[title][0]["pos"])):
        px, py, pz = JsonDecoder.get_vert_data(json_data[title][0]["pos"][i])
        m_vertex = Vertex(px, py, pz)
        vertices.append(m_vertex)

    indices = []
    for i in range(len(json_data[title][0]["indices"])):
        indices.append(json_data[title][0]["indices"][i])

    geometry_data = MeshGeometry(vertices=vertices, indices=indices)
    return geometry_data
