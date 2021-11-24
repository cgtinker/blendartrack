import bpy
import importlib
# https://blender.stackexchange.com/questions/36902/how-to-keyframe-mesh-vertices-in-python
from ..blend import keyframe

importlib.reload(keyframe)


def animate_geometry(obj, frames, positions):
    frames.append(len(frames) + 1)
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
        f_curves.append([f_curve, vertex])
    """
    # splitting xyz positions
    x_p = [x[0] for x in positions]
    y_p = [y[1] for y in positions]
    z_p = [z[2] for z in positions]
    xyz_pos = [x_p, y_p, z_p]
    
    for f_curve in f_curves:
        for i, fc_data in enumerate(zip(f_curve, xyz_pos)):
            # populate keyframes
            #fc_data[0].keyframe_points.add(count=len(frames))

            print("co", [x for co in zip(frames, fc_data[1][i]) for x in co])
            print(len(frames), len(fc_data[1]))
            #fc_data[0].keyframe_points.foreach_set("co", [x for co in zip(frames, fc_data[1][i]) for x in co])
            fc_data[0].update()
   
    # inserting to fcurves
    for f_curve, vertex in f_curves:
        for i, fc in enumerate(f_curve):
            # populate points
            fc.keyframe_points.add(count=len(frames))
            # set keyframe position per channel
            fc.keyframe_points.foreach_set(
                f"vertices[{i}].co",
                [x for co in zip(frames, xyz_pos[i]) for x in co]
            )
            fc.update()
        # assign animation data
        vertex.update_tag(refresh={'DATA'})
   
    """
    # adding animation data
    for frame in frames:
        print("retargeting face mesh geometry at frame ", frame, end='\r')
        for i in range(len(positions[frame-1])):
            keyframe.keyframe_geometry(f_curves[i], frame, positions[frame - 1][i])
            obj.update_tag(refresh={'DATA'})
