import bmesh
import bpy


def init_face_mesh(vertices, faces, uvs, scene):
    bm = bmesh.new()

    # set vertices
    for v in vertices:
        bm.verts.new((v[0], v[1], v[2]))

    # required for accessing vertex data
    bm.verts.ensure_lookup_table()
    bm.verts.index_update()

    # set faces
    for f in faces:
        bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))

    bm.normal_update()

    # set uvs
    uv_layer = bm.loops.layers.uv.new()
    for face in bm.faces:
        for loop in face.loops:
            loop[uv_layer].uv = uvs[loop.vert.index]

    # init mesh
    mesh = bpy.data.meshes.new("r_face_mesh")
    bm.to_mesh(mesh)
    bm.free()

    # init obj
    obj = bpy.data.objects.new("r_face_mesh", mesh)

    # smooth shading
    mesh = obj.data
    for f in mesh.polygons:
        f.use_smooth = True

    # making object available
    scene.collection.objects.link(obj)

    return obj
