import bpy
import importlib
from bpy.types import Operator
from management import event_listener

importlib.reload(event_listener)


class UI_import_button(Operator):
    bl_label = "Import Data"
    bl_idname = "button.import_tracking_data"
    bl_description = "Import data from file path"

    def execute(self, context):
        user = context.scene.m_cgtinker_blendartrack
        event_listener.file_to_load(bpy.path.abspath(user.data_path))
        return {'FINISHED'}


class UI_internal_compositing(Operator):
    bl_label = "Internal Compositing"
    bl_idname = "button.internal_compositing"
    bl_description = "Setup an internal composition with the active camera."

    def execute(self, context):
        event_listener.internal_compositing()
        return {'FINISHED'}


class UI_external_compositing(Operator):
    bl_label = "External Compositing"
    bl_idname = "button.external_compositing"
    bl_description = "Setup scene renderer for external compositing."

    def execute(self, context):
        event_listener.external_compositing()
        return {'FINISHED'}


class UI_base_rig(Operator):
    bl_label = "Base Rig"
    bl_idname = "button.base_rig"
    bl_description = ""

    def execute(self, context):
        print("copy rig selected")
        return {'FINISHED'}


class UI_driver_rig(Operator):
    bl_label = "Driver Rig"
    bl_idname = "button.driver_rig"
    bl_description = ""

    def execute(self, context):
        print("driver rig selected")
        return {'FINISHED'}


class UI_copy_to_rig(Operator):
    bl_label = "Copy Rig"
    bl_idname = "button.copy_rig"
    bl_description = ""

    def execute(self, context):
        print("copy rig selected")
        return {'FINISHED'}
