import bpy
import importlib
import os
import sys

from bpy.props import (StringProperty, BoolProperty, PointerProperty)
from bpy.types import (Panel, Operator, PropertyGroup)
from bpy_extras.io_utils import ImportHelper

from . import EventListner
importlib.reload(EventListner)


bl_info = {
    "name": "retargeter",
    "description": "",
    "author": "cgtinker",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "3D View > Tool",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

# append sys path to dir
main_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'module')
sys.path.append(main_dir)


# ------------------------------------------------------------------------
#    FileBrowser
# ------------------------------------------------------------------------

public_filename = ""


class OpenFilebrowser(Operator, ImportHelper):
    bl_idname = "open_filebrowser"
    bl_label = "Open the file browser"

    filter_glob: StringProperty(
        default='*.zip;*;*.json',
        options={'HIDDEN'}
    )

# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------


class MyProperties(PropertyGroup):
    my_path: StringProperty(
        name="Import Data",
        description="Choose a .zip or .json file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class UI_retarget_button(Operator):
    bl_label = "Start Retargeting"
    bl_idname = "button.start_retargeting"

    def execute(self, context):
        scene = context.scene
        filebrowser = scene.m_importer
        EventListner.file_to_load(bpy.path.abspath(filebrowser.my_path))

        return {'FINISHED'}

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class UI_custom_panel(Panel):
    bl_label = "Retargeter"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Retargeter"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        filebrowser = scene.m_importer

        layout.prop(filebrowser, "my_path")
        layout.operator("button.start_retargeting")


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    MyProperties,
    UI_retarget_button,
    UI_custom_panel
)


def register():
    from bpy.utils import register_class
    for m_class in classes:
        register_class(m_class)

    print("Retargeter Initialized")
    bpy.types.Scene.m_importer = PointerProperty(type=MyProperties)


def unregister():
    from bpy.utils import unregister_class
    for m_class in reversed(classes):
        unregister_class(m_class)
    del bpy.types.Scene.m_importer


if __name__ == "__main__":
    register()
