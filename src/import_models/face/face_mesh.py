from .. import iCustomData
from ...utils.json import decoder
from ...utils.blend import name, scene, collection
from ...utils.blend import constraints
from ...utils.mapping import CreateBMesh
from ...utils import reference_names


class FaceMesh(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.batch = batch
        self.title = title

        self.model = None
        self.name = reference_names.ar_face
        self.parent_name = reference_names.face_parent
        self.collection_name = reference_names.face_col
        self.face_object = None

    def initialize(self):
        vertices = []
        for i in range(len(self.json_data[self.title][0]["pos"])):
            px, py, pz = decoder.get_vert_data(self.json_data[self.title][0]["pos"][i])
            vertices.append(Vertex(px, py, pz))

        indices = []
        for i in range(len(self.json_data[self.title][0]["indices"])):
            indices.append(self.json_data[self.title][0]["indices"][i])

        uvs = []
        for i in range(len(self.json_data[self.title][0]["uvs"])):
            px, py = decoder.get_two_dim_data(self.json_data[self.title][0]["uvs"][i])
            uvs.append(UV(px, py))

        self.model = MeshGeometry(vertices=vertices, indices=indices, uvs=uvs)

    # TODO: Check for user input before!!! ["MESH"]
    def generate(self):
        self.name = name.set_reference_name(self.name)

        if self.model is None:
            print("model not imported correctly")
            return

        self.set_geometry()

    def animate(self):
        pass

    def structure(self):
        if self.batch:
            parent = name.get_object_by_name(name=self.parent_name)
            self.set_constraints(self.face_object, parent)

            collection.add_obj_to_collection(self.collection_name, self.face_object)

    def set_geometry(self):
        active_scene = scene.get_scene()

        vertices = self.model.get_vertices()
        faces = self.model.get_faces()
        uvs = self.model.get_uvs()
        self.face_object = CreateBMesh.create_b_mesh(vertices, faces, uvs, active_scene, self.name)

    @staticmethod
    def set_constraints(obj, parent):
        constraints.add_copy_location_constraint(obj=obj, target_obj=parent, use_offset=True)
        constraints.add_copy_rotation_constraint(obj=obj, target_obj=parent, invert_y=False)


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