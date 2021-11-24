import bpy
import importlib
from bpy.types import Operator
from ..management import input_manager

importlib.reload(input_manager)


class UI_import_button(Operator):
    bl_label = "Import Data"
    bl_idname = "button.import_tracking_data"
    bl_description = "Import data from file path"

    def execute(self, context):
        user = context.scene.m_cgtinker_blendartrack
        input_manager.file_to_load(bpy.path.abspath(user.data_path))
        return {'FINISHED'}


class UI_internal_compositing(Operator):
    bl_label = "Internal Compositing"
    bl_idname = "button.internal_compositing"
    bl_description = "Setup an internal composition with the active camera."

    def execute(self, context):
        input_manager.internal_compositing()
        return {'FINISHED'}


class UI_external_compositing(Operator):
    bl_label = "External Compositing"
    bl_idname = "button.external_compositing"
    bl_description = "Setup scene renderer for external compositing."

    def execute(self, context):
        input_manager.external_compositing()
        return {'FINISHED'}


class UI_base_rig(Operator):
    bl_label = "Base Rig"
    bl_idname = "button.face_rig"
    bl_description = ""

    def execute(self, context):
        input_manager.generate_face_rig()
        return {'FINISHED'}


class UI_driver_rig(Operator):
    bl_label = "Driver Rig"
    bl_idname = "button.driver_rig"
    bl_description = ""

    def execute(self, context):
        input_manager.generate_driver_rig()
        return {'FINISHED'}


class UI_diver_update(Operator):
    bl_label = "Driver Update"
    bl_idname = "button.driver_update"
    bl_description = ""

    def execute(self, context):
        input_manager.update_driver_influence()
        return {'FINISHED'}


class UI_copy_to_rig(Operator):
    bl_label = "Copy Rig"
    bl_idname = "button.copy_rig"
    bl_description = ""

    def execute(self, context):
        input_manager.transfer_rig()
        return {'FINISHED'}
