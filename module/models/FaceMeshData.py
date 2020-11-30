from .helper import KeyframeAssistent, JsonDecoder
import importlib

importlib.reload(KeyframeAssistent)
importlib.reload(JsonDecoder)


class FaceMesh:
    def __init__(self, mesh_vertices, frame):
        self.vertices = mesh_vertices
        self.frame = frame

    def init_frame(self, scene):
        KeyframeAssistent.init_keyframe(self.frame, scene)
        print("retargeting face mesh data at frame ", self.frame, end='\r')

    def key_pos(self, objects):
        for i in range(len(self.vertices)):
            self.vertices[i].key_pos(objects[i])

    def print_content(self):
        print("frame:", self.frame)
        for mesh_vertex in self.vertices:
            mesh_vertex.print_vert_content()


class MeshVertex:
    def __init__(self, px, py, pz):
        self.px = px
        self.py = pz    # fixing unity coordinate system
        self.pz = py    # fixing unity coordinate system

    def key_pos(self, obj):
        KeyframeAssistent.set_pos_keyframe(self.px * 10, self.py * 10, self.pz * 10, obj)

    def print_vert_content(self):
        print('vert: px', self.px, 'vert: py', self.py, 'vert: pz', self.pz)


def init_mesh_model(json_data):
    # array to store pose data
    mesh_model = []
    # decoding json
    for data in json_data['meshDataList']:
        frame = data['frame']
        # vertex array to recreate the face mesh
        mesh_vertices = []
        for i in range(len(data['pos'])):
            px, py, pz = JsonDecoder.get_vert_data(data['pos'][i])
            m_vertex = MeshVertex(px, py, pz)
            mesh_vertices.append(m_vertex)
        # storing vertex array and frame
        tmp = FaceMesh(mesh_vertices, frame)
        mesh_model.append(tmp)
    return mesh_model
