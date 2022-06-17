import bpy
import importlib
# https://blender.stackexchange.com/questions/36902/how-to-keyframe-mesh-vertices-in-python
from ..blend import keyframe

importlib.reload(keyframe)


def new_loc_struct(model):
    # todo: make priv method for empties and face mesh
    vertex_pos_data = []
    for index, _ in enumerate(model[0].vertices):
        vertex_px = []
        vertex_py = []
        vertex_pz = []
        # for all data in model
        for data in model:
            pos = data.vertices[index].get_pos()
            vertex_px.append(pos[0])
            vertex_py.append(pos[1])
            vertex_pz.append(pos[2])
        vertex_pos_data.append([vertex_px, vertex_py, vertex_pz])
    return vertex_pos_data


def animate_geometry(obj, frames, model):
    m_positions = new_loc_struct(model)

    mesh = obj.data

    action = bpy.data.actions.new("m_MeshAnimation")
    # new action animation data
    mesh.animation_data_create()
    mesh.animation_data.action = action

    # location anim path
    data_path = "vertices[%d].co"

    f_curves = []
    for v_index, vertex in enumerate(mesh.vertices):
        f_curve = [action.fcurves.new(
            data_path=data_path % vertex.index,
            index=i) for i in range(3)]

        for f_index, fc in enumerate(f_curve):
            fc.keyframe_points.add(count=len(frames))
            fc.keyframe_points.foreach_set("co", [x for co in zip(frames, m_positions[v_index][f_index]) for x in co])
            fc.update()


def old_geometry_animation(obj, frames, positions):
    # get mesh
    mesh = obj.data
    action = bpy.data.actions.new("m_MeshAnimation")

    # new action animation data
    mesh.animation_data_create()
    mesh.animation_data.action = action

    # location anim path
    data_path = "vertices[%d].co"

    f_curves = []
    for vertex in mesh.vertices:
        f_curve = [action.fcurves.new(
            data_path=data_path % vertex.index,
            index=i) for i in range(3)]
        f_curves.append(f_curve)

    # adding animation data
    for frame in frames:
        print("retargeting face mesh geometry at frame ", frame, end='\r')
        for i in range(len(positions[frame - 1])):
            keyframe.keyframe_geometry(f_curves[i], frame, positions[frame - 1][i])
            obj.update_tag(refresh={'DATA'})
