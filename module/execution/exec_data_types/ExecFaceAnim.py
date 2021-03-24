from module.execution.objects import ReferenceObject, KeyframeAssistent, Name
from module.execution.scene import Scene
from module.mapping import VertexAnimation
import bpy
from importlib import reload
reload(ReferenceObject)
reload(KeyframeAssistent)
reload(Scene)
reload(VertexAnimation)
reload(Name)


def exec_face_anim(model, batch, name, parent_name):
    print("importing face mesh model")
    get_user_input = bpy.context.scene.m_cgtinker_blendartrack
    if get_user_input.enum_face_type == 'MESH':
        animate_geometry(model, name)

    else:
        animate_empties(batch, model, parent_name)


def animate_geometry(model, name):
    mesh = Name.get_object_by_name(name)
    frames = []
    positions = []
    for data in model:
        frames.append(data.frame)
        positions.append(data.get_positions())
    VertexAnimation.animate_geometry(mesh, frames, positions)


def animate_empties(batch, model, parent_name):
    active_scene, parent = init_face_mesh_empties(model, batch, parent_name)
    # generating empties
    reference_objects = ReferenceObject.generate_empties((len(model[0].vertices)), size=0.0025)
    # key framing empties
    for data in model:
        # data.init_frame(active_scene)
        KeyframeAssistent.init_keyframe(data.frame, active_scene)
        for i in range(len(data.vertices)):
            if data.vertices:
                pos = data.vertices[i].get_pos()
                KeyframeAssistent.set_pos_keyframe(
                    pos[0], pos[1], pos[2], reference_objects[i])
    # setting parent
    for obj in reference_objects:
        obj.parent = parent
    # disabling debug lines to parent
    # active_scene.disable_relation_lines()


def init_face_mesh_empties(model, batch, parent_name):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        parent = Name.get_object_by_name(name=parent_name)
    else:
        parent = ReferenceObject.generate_empty_at(
            px=0, py=0, pz=0, size=1, name=parent_name)

    return active_scene, parent
