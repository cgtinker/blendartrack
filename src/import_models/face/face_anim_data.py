from ...utils.json import decoder


class MeshVertices:
    def __init__(self, mesh_vertices, frame):
        self.vertices = mesh_vertices
        self.frame = frame

    def get_positions(self):
        vertices = []
        for i in range(len(self.vertices)):
            if self.vertices:
                vertices.append(self.vertices[i].get_pos())
        return vertices

    def print_contents(self):
        vertices = []
        for mesh_vertex in self.vertices:
            vertices.append(mesh_vertex.__repr__())
        return f'frame: {self.frame}, vertices: {self.vertices}'


class MeshVertex:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def get_pos(self):
        return [self.px, self.py, self.pz]

    def __repr__(self):
        return f'x: {self.px}, y: {self.py}, z: {self.pz}'


def initialize(json_data, title):
    # set frame and vertex location data as mesh model
    model = []
    for data in json_data[title]:
        frame = data['frame']
        # vertex array to recreate the face mesh
        mesh_vertices = []
        for i in range(len(data['pos'])):
            px, py, pz = decoder.get_vert_data(data['pos'][i])
            m_vertex = MeshVertex(px, py, pz)
            mesh_vertices.append(m_vertex)
        # storing vertex array at frame
        tmp = MeshVertices(mesh_vertices, frame)
        model.append(tmp)
    return model
