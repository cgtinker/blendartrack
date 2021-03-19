import bpy

# https://blender.stackexchange.com/questions/36902/how-to-keyframe-mesh-vertices-in-python
# thanks to pink vertex and batFINGER to get me started


def insert_keyframe(f_curves, frame, positions):
    for fcu, position in zip(f_curves, positions):
        fcu.keyframe_points.insert(frame, position, options={'FAST'})


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
            insert_keyframe(f_curves[i], frame, positions[frame-1][i])
