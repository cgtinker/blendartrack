bl_info = {
    "name": "blendartrack",
    "description": "",
    "author": "cgtinker",
    "version": (0, 5, 2),
    "blender": (2, 90, 0),
    "location": "3D View > Tool",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}


import bpy
import importlib
import os
import sys
'''
# getting access to the current dir - necessary to access blender file location (manual debugging)
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)
'''
from bpy.types import PropertyGroup
from bpy.props import (StringProperty,
                       PointerProperty,
                       BoolProperty,
                       EnumProperty
                       )
from .module.interface import (Operators,
                              Panels,
                              Properties)

importlib.reload(Operators)
importlib.reload(Panels)
importlib.reload(Properties)


# append sys path to dir
main_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'module')
sys.path.append(main_dir)


class MyProperties(PropertyGroup):
    data_path: StringProperty(
        name="File Path",
        description="File path to .zip or .json file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

    button_import_text: StringProperty(
        name="Import Data",
        description="Button Display Text",
        default="Import Data"
    )

    bool_point_cloud: BoolProperty(
        name="Point Cloud",
        description="Dots recognized during the tracking process",
        default=True
    )

    bool_reference_point: BoolProperty(
        name="Reference Points",
        description="Reference points placed during the tracking process",
        default=True
    )

    enum_face_type: EnumProperty(
        name="",
        description="Either import an animated face mesh or animated empties",
        items=[('MESH', "Face Mesh", "Import an animated face mesh"),
               ('EMPTIES', "Animated Empties", "Import animated empties")]
    )


classes = (
    MyProperties,
    Operators.UI_import_button,
    Panels.UI_main_panel
)


def register():
    from bpy.utils import register_class
    for m_class in classes:
        register_class(m_class)

    print("Blendartrack Initialized")
    bpy.types.Scene.m_cgtinker_blendartrack = PointerProperty(type=MyProperties)


def unregister():
    from bpy.utils import unregister_class
    for m_class in reversed(classes):
        unregister_class(m_class)
    del bpy.types.Scene.m_cgtinker_blendartrack


if __name__ == "__main__":
    register()
