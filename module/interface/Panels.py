import bpy
from bpy.types import Panel
from . import Properties

import importlib


importlib.reload(Properties)


class DefaultPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}


class BLENDARTRACK_PT_MainPanel(DefaultPanel, bpy.types.Panel):
    bl_idname = "BLENDARTRACK_PT_parent_panel"
    bl_label = "BlendArTrack"

    def draw(self, context):
        scene = bpy.context.scene
        my_tool = scene.my_tool

        layout = self.layout
        layout.label(text="This is the main panel.")

        layout.prop(my_tool, "my_int")
        layout.prop(my_tool, "my_bool")


class BLENDARTRACK_PT_CameraPanel(DefaultPanel, bpy.types.Panel):
    bl_parent_id = "BLENDARTRACK_PT_parent_panel"
    bl_label = "Camera Tracking"

    def draw(self, context):
        layout = self.layout
        layout.label(text="First Sub Panel of Panel 1.")


class BLENDARTRACK_PT_FacePanel(DefaultPanel, bpy.types.Panel):
    bl_parent_id = "BLENDARTRACK_PT_parent_panel"
    bl_label = "Face Tracking"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Second Sub Panel of Panel 1.")


classes = (
    Properties.ImportProperties,
    Properties.WM_OT_HelloWorld,
    BLENDARTRACK_PT_MainPanel,
    BLENDARTRACK_PT_CameraPanel,
    BLENDARTRACK_PT_FacePanel
)


class OBJECT_PT_CustomPanel(Panel):
    bl_label = "My Panel"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools"
    bl_context = "objectmode"

    @classmethod
    def poll(self, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "my_enum", text="")
        layout.prop(mytool, "my_bool")
        layout.prop(mytool, "my_int")
        layout.prop(mytool, "my_float")
        layout.prop(mytool, "my_float_vector", text="")
        layout.prop(mytool, "my_string")
        layout.prop(mytool, "my_path")
        layout.operator("wm.hello_world")
        layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()