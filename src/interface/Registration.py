import bpy
from bpy.props import PointerProperty
from . import Panels
from . import Properties, Operators

import importlib
importlib.reload(Operators)
importlib.reload(Panels)
importlib.reload(Properties)

classes = (
    Properties.MyProperties,

    Operators.UI_import_button,
    Operators.UI_internal_compositing,
    Operators.UI_external_compositing,
    Operators.UI_base_rig,
    Operators.UI_driver_rig,
    Operators.UI_copy_to_rig,
    Operators.UI_diver_update,

    Panels.UI_PT_main_panel,
    Panels.UI_PT_compositing_panel,
    Panels.UI_PT_face_rigging_panel,
)


def register(properties):
    from bpy.utils import register_class
    for m_class in classes:
        print(m_class)
        register_class(m_class)

    bpy.types.Scene.m_cgtinker_blendartrack = PointerProperty(type=properties)


def unregister():
    from bpy.utils import unregister_class
    for m_class in reversed(classes):
        print(m_class)
        unregister_class(m_class)
    del bpy.types.Scene.m_cgtinker_blendartrack
