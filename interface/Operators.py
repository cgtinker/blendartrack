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
        cgt = context.scene.m_cgtinker_blendartrack
        event_listener.file_to_load(bpy.path.abspath(cgt.data_path))
        return {'FINISHED'}




