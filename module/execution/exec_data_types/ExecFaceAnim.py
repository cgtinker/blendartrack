from . import ExecFaceEmpties
from ..objects import ReferenceObject, KeyframeAssistent, Name
from ..scene import Scene
from ...mapping import VertexAnimation
import bpy
from importlib import reload
reload(ReferenceObject)
reload(KeyframeAssistent)
reload(Scene)
reload(VertexAnimation)
reload(Name)


def exec_face_anim(model, batch, name, parent_name, empty_col):
    print("importing face mesh model")
    get_user_input = bpy.context.scene.m_cgtinker_blendartrack
    if get_user_input.enum_face_type == 'MESH':
        animate_geometry(model, name)

    else:
        ExecFaceEmpties.animate_empties(batch, model, parent_name, empty_col)


def animate_geometry(model, name):
    mesh = Name.get_object_by_name(name)
    frames = []
    positions = []
    for data in model:
        frames.append(data.frame)
        positions.append(data.get_positions())
    VertexAnimation.animate_geometry(mesh, frames, positions)
