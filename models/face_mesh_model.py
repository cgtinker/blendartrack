from utils.custom_data.iCustomData import ImportModel
from utils.json import decoder


class FaceMeshModel(ImportModel):
    def __init__(self, json_data, title):
        self.json_data = json_data
        self.title = title
        self.mesh_model = []

    def initialize(self):
        for data in self.json_data[self.title]:
            frame = data['frame']
            # vertex array to recreate the face mesh
            mesh_vertices = []
            for i in range(len(data['pos'])):
                px, py, pz = decoder.get_vert_data(data['pos'][i])
                m_vertex = MeshVertex(px, py, pz)
                mesh_vertices.append(m_vertex)
            # storing vertex array and frame
            tmp = FaceMesh(mesh_vertices, frame)
            self.mesh_model.append(tmp)
        # Todo: validate set list
        self.mesh_model = set(self.mesh_model)

    def prepare(self, model, batch):
        pass

    def execute(self):
        pass


class FaceMesh:
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
        print("frame:", self.frame)
        for mesh_vertex in self.vertices:
            mesh_vertex.print_vert_content()


class MeshVertex:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def get_pos(self):
        return [self.px, self.py, self.pz]

    def print_vert_content(self):
        print('vert: px', self.px, 'vert: py', self.py, 'vert: pz', self.pz)



