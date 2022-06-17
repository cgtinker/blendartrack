import bmesh
import bpy

import src.utils.blend.objects


def create_b_mesh(vertices, faces, uvs, scene, name):
    bm = bmesh.new()
    set_bm_geometry(bm, faces, uvs, vertices)

    mesh = init_mesh(bm, name)
    obj = bpy.data.objects.new(name, mesh)
    smooth_shading(obj)

    src.utils.blend.objects.objects.link(obj)
    return obj


def set_bm_geometry(bm, faces, uvs, vertices):
    set_vertices(bm, vertices)
    set_faces(bm, faces)
    set_uvs(bm, uvs)


def set_uvs(bm, uvs):
    uv_layer = bm.loops.layers.uv.new()
    for face in bm.faces:
        for loop in face.loops:
            loop[uv_layer].uv = uvs[loop.vert.index]


def set_faces(bm, faces):
    for f in faces:
        bm.faces.new((bm.verts[f[0]], bm.verts[f[1]], bm.verts[f[2]]))
    bm.normal_update()


def set_vertices(bm, vertices):
    for v in vertices:
        bm.verts.new((v[0], v[1], v[2]))
    # required for accessing vertex data
    bm.verts.ensure_lookup_table()
    bm.verts.index_update()


def init_mesh(bm, name):
    mesh = bpy.data.meshes.new(name)
    bm.to_mesh(mesh)
    bm.free()
    return mesh


def smooth_shading(obj):
    mesh = src.utils.blend.objects.data
    for f in mesh.polygons:
        f.use_smooth = True

