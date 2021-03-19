import module.execution.objects.Name
from module.execution.objects import ReferenceObject
from module.execution.scene import Scene
from module.mapping import CreateBMesh
import importlib
importlib.reload(CreateBMesh)
importlib.reload(Scene)


def exec_face_geometry(model, batch, name):
    print("import face mesh geometry")
    active_scene = Scene.get_scene_context()
    vertices = model.get_vertices()
    faces = model.get_faces()
    uvs = model.get_uvs()
    obj = CreateBMesh.create_b_mesh(vertices, faces, uvs, active_scene, name)
    if batch:
        parent = module.execution.objects.Name.get_object_by_name(name="Retarget_Face_Pos")
        obj.parent = parent
