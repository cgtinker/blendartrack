import bpy
from bpy.props import PointerProperty


def register(classes, properties):
    from bpy.utils import register_class
    for m_class in classes:
        register_class(m_class)

    print("Blendartrack Initialized")
    bpy.types.Scene.m_cgtinker_blendartrack = PointerProperty(type=properties)


def unregister(classes):
    from bpy.utils import unregister_class
    for m_class in reversed(classes):
        unregister_class(m_class)
    del bpy.types.Scene.m_cgtinker_blendartrack
