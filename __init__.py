import bpy
import importlib
import os
import sys

# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)

from bpy.types import (PropertyGroup,
                       Panel,
                       Operator)

from bpy.props import (StringProperty,
                       BoolProperty,
                       EnumProperty,
                       PointerProperty
                       )

from bpy_extras.io_utils import ImportHelper

from module import EventListner

importlib.reload(EventListner)


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
    data_path: StringProperty(
        name="File Path",
        description="File path to .zip or .json file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
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


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class UI_import_button(Operator):
    bl_label = "Import Tracking Data"
    bl_idname = "button.import_tracking_data"

    def execute(self, context):
        scene = context.scene
        cgtinker_blendartrack = scene.m_cgtinker_blendartrack

        EventListner.file_to_load(bpy.path.abspath(cgtinker_blendartrack.data_path))

        return {'FINISHED'}

# ------------------------------------------------------------------------
#    Panels
# ------------------------------------------------------------------------


class DefaultPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "blendartrack"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}


class UI_main_panel(DefaultPanel, Panel):
    bl_label = "blendartrack"
    bl_idname = "OBJECT_PT_parent_panel"

    def draw(self, context):
        layout = self.layout
        cgtinker_blendartrack = context.scene.m_cgtinker_blendartrack

        # file path
        layout.prop(cgtinker_blendartrack, "data_path")
        layout.split(factor=1.0, align=False)

        # camera tracking data option
        cam = layout.box()
        cam.label(text="Camera Track Import Options") # , icon='EMPTY_DATA')
        cam.prop(cgtinker_blendartrack, "bool_point_cloud")
        cam.prop(cgtinker_blendartrack, "bool_reference_point")
        layout.split(factor=1.0, align=False)

        # face tracking data options
        face = layout.box()
        face.label(text="Face Track Import Options") # , icon='MESH_DATA')
        face.prop(cgtinker_blendartrack, "enum_face_type")
        layout.split(factor=2.0, align=False)

        # import button
        layout.operator("button.import_tracking_data")


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------


classes = (
    MyProperties,
    UI_import_button,
    UI_main_panel
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
