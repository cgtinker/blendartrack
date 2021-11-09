import bpy
import importlib
# https://blender.stackexchange.com/questions/36902/how-to-keyframe-mesh-vertices-in-python
from ..blend import keyframe

importlib.reload(keyframe)


def animate_geometry(obj, frames, positions):
    # get mesh
    mesh = obj.data
    action = bpy.data.actions.new("m_MeshAnimation")

    # new action animation data
    mesh.animation_data_create()
    mesh.animation_data.action = action

    # location anim path
    data_path = "vertices[%d].co"

    # f_curves for mesh vertices
    f_curves = []
    for vertex in mesh.vertices:
        f_curve = [action.fcurves.new(
            data_path=data_path % vertex.index,
            index=i) for i in range(3)]
        f_curves.append(f_curve)

    # adding animation data
    for frame in frames:
        print("retargeting face mesh geometry at frame ", frame, end='\r')
        for i in range(len(positions[frame-1])):
            keyframe.keyframe_geometry(f_curves[i], frame, positions[frame - 1][i])
            obj.update_tag(refresh={'DATA'})
