import bpy
from bpy.props import PointerProperty
from . import cgt_operators, cgt_panels
from .cgt_properties import BlendArTrackProperties

classes = (
    BlendArTrackProperties,

    cgt_operators.UI_import_button,
    cgt_operators.UI_internal_compositing,
    cgt_operators.UI_external_compositing,
    cgt_operators.UI_base_rig,
    cgt_operators.UI_driver_rig,
    cgt_operators.UI_copy_to_rig,
    cgt_operators.UI_diver_update,
    cgt_operators.UI_smooth_selected_objects,

    cgt_panels.UI_PT_main_panel,
    cgt_panels.UI_PT_compositing_panel,
    cgt_panels.UI_PT_face_rigging_panel,
)


def register():
    from bpy.utils import register_class
    #from .. import cgt_imports
    print("Register BlendArTrack\n")
    for m_class in classes:
        register_class(m_class)
    #cgt_imports.manage_imports(False)
    bpy.types.Scene.m_cgtinker_blendartrack = PointerProperty(type=BlendArTrackProperties)


def unregister():
    print("Unregister BlendArTrack")
    from bpy.utils import unregister_class
    for m_class in reversed(classes):
        # print(m_class)
        unregister_class(m_class)
    del bpy.types.Scene.m_cgtinker_blendartrack
