from ..mapping import CreateBMesh
from ..execution.objects import KeyframeAssistent
from ..preperation.importing import DecodeJson

import importlib
importlib.reload(KeyframeAssistent)
importlib.reload(DecodeJson)
importlib.reload(CreateBMesh)


class MeshGeometry:
    def __init__(self, vertices, indices, uvs):
        self.vertices = vertices
        self.indices = indices
        self.uvs = uvs

    def get_vertices(self):
        m_vertices = []
        for i in range(len(self.vertices)):
            m_vertex = self.vertices[i].get_vertex()
            m_vertices.append(m_vertex)
        return m_vertices

    def get_faces(self):
        faces = (list(self.chunks(self.indices, 3)))
        return faces

    def get_uvs(self):
        m_uvs = []
        for i in range(len(self.uvs)):
            m_uv = self.uvs[i].get_uv()
            m_uvs.append(m_uv)
        return m_uvs

    @staticmethod
    def chunks(lst, n):
        # yields successive n-sized chunks from lst.
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    def print_contents(self):
        for index in self.indices:
            print(index)
        for mesh_vertex in self.vertices:
            mesh_vertex.print_vert_content()
        for uv in self.uvs:
            uv.print_uv_content()


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


class UV:
    def __init__(self, px, py):
        self.px = px
        self.py = py

    def get_uv(self):
        m_uv = (self.px, self.py)
        return m_uv

    def print_uv_content(self):
        print("px:", self.px, "py:", self.py)


# decoding json
def init_mesh_geo_model(json_data, title):
    vertices = []
    for i in range(len(json_data[title][0]["pos"])):
        px, py, pz = DecodeJson.get_vert_data(json_data[title][0]["pos"][i])
        vertices.append(Vertex(px, py, pz))

    indices = []
    for i in range(len(json_data[title][0]["indices"])):
        indices.append(json_data[title][0]["indices"][i])

    uvs = []
    for i in range(len(json_data[title][0]["uvs"])):
        px, py = DecodeJson.get_two_dim_data(json_data[title][0]["uvs"][i])
        uvs.append(UV(px, py))

    geometry_data = MeshGeometry(vertices=vertices, indices=indices, uvs=uvs)
    return geometry_data
