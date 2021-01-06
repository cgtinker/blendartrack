import bmesh
import bpy


def init_face_mesh(vertices, faces, scene):
    bm = bmesh.new()

    # adding vertices
    for v in vertices:
        bm.verts.new((v[0], v[1], v[2]))
    bm.verts.ensure_lookup_table()

    # adding faces
    for f in faces:
        bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))
    bm.normal_update()

    # init mesh
    mesh = bpy.data.meshes.new("face_mesh")
    bm.to_mesh(mesh)
    bm.free()

    # init obj
    obj = bpy.data.objects.new("face_mesh", mesh)
    scene.collection.objects.link(obj)
