import bpy
from bpy.props import PointerProperty
from interface import Operators
from interface import Properties, Panels
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
<<<<<<< HEAD
    Panels.UI_PT_compositing_panel,
    Panels.UI_PT_face_rigging_panel,
=======
    Panels.UI_PT_camera_panel,
    Panels.UI_PT_main_panel_extension,
    Panels.UI_PT_face_panel,
    Panels.UI_PT_face_rigging_panel
>>>>>>> 03cdd482d47a39126b818d7f0ab697862a41436d
)


def register(properties):
    from bpy.utils import register_class
    for m_class in classes:
        register_class(m_class)

    print("Blendartrack Initialized")
    bpy.types.Scene.m_cgtinker_blendartrack = PointerProperty(type=properties)


def unregister():
    from bpy.utils import unregister_class
    for m_class in reversed(classes):
        unregister_class(m_class)
    del bpy.types.Scene.m_cgtinker_blendartrack
