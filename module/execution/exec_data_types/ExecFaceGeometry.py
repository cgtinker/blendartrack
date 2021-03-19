from module.execution.processing.objects import ReferenceObject
from module.execution.processing.scene import Scene
from module.execution.processing.data_mapping import CreateBMesh


def exec_face_geometry(batch, model):
    print("import face mesh geometry")
    active_scene = Scene.get_scene_context()
    vertices = model.get_vertices()
    faces = model.get_faces()
    uvs = model.get_uvs()
    obj = CreateBMesh.create_b_mesh(vertices, faces, uvs, active_scene)
    if batch:
        parent = ReferenceObject.get_object_by_name(name="Retarget_Face_Pos")
        obj.parent = parent