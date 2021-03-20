from module.execution.objects import Constraints, Name
from module.execution.scene import Scene, Collections
from module.mapping import CreateBMesh
from importlib import reload

reload(CreateBMesh)
reload(Scene)
reload(Name)
reload(Collections)
reload(Constraints)


def exec_face_geometry(model, batch, name, parent, col_name):
    print("import face mesh geometry")
    active_scene = Scene.get_scene_context()
    obj = set_geometry(active_scene, model, name)
    if batch:
        parent = Name.get_object_by_name(name=parent)
        set_constraints(obj, parent)

    Collections.add_obj_to_collection(col_name, obj)


def set_constraints(m_object, parent):
    Constraints.add_copy_location_constraint(obj=m_object, target_obj=parent, use_offset=True)
    Constraints.add_copy_rotation_constraint(obj=m_object, target_obj=parent, invert_y=False)


def set_geometry(active_scene, model, name):
    vertices = model.get_vertices()
    faces = model.get_faces()
    uvs = model.get_uvs()
    obj = CreateBMesh.create_b_mesh(vertices, faces, uvs, active_scene, name)
    return obj
