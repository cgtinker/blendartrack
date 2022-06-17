import bpy
from mathutils import Matrix

import src.utils.blend.objects


def apply_transfrom(ob, use_location=False, use_rotation=False, use_scale=False):
    mb = ob.matrix_basis
    I = Matrix()
    loc, rot, scale = mb.decompose()

    # rotation
    T = Matrix.Translation(loc)
    #R = rot.to_matrix().to_4x4()
    R = mb.to_3x3().normalized().to_4x4()
    S = Matrix.Diagonal(scale).to_4x4()

    transform = [I, I, I]
    basis = [T, R, S]

    def swap(i):
        transform[i], basis[i] = basis[i], transform[i]

    if use_location:
        swap(0)
    if use_rotation:
        swap(1)
    if use_scale:
        swap(2)
        
    M = transform[0] @ transform[1] @ transform[2]
    if hasattr(src.utils.blend.objects.data, "transform"):
        src.utils.blend.objects.data.transform(M)
    for c in ob.children:
        c.matrix_local = M @ c.matrix_local
        
    ob.matrix_basis = basis[0] @ basis[1] @ basis[2]


# move bpy obj function to utils.blend
def select_object(obj):
    for ob in bpy.context.selected_objects:
        ob.select_set(False)
    obj.select_set(True)
    return obj


def get_object_by_name(name):
    obj = bpy.data.objects[name]
    return obj


# todo: should be in blend utils
def apply_transforms_to_object(obj):
    select_object(obj)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
