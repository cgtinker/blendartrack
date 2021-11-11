from bpy.types import Panel
import bpy

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
        user = context.scene.m_cgtinker_blendartrack

        # draw layout
        self.path_prop_layout(user)
        self.camera_layout(user)
        self.face_layout(user)
        self.import_btn(user)

    def path_prop_layout(self, user):
        self.layout.prop(user, "data_path")
        self.layout.split(factor=1.0, align=False)

    def camera_layout(self, user):
        cam = self.layout.box()
        cam.label(text="Camera Track Import Options")  # , icon='EMPTY_DATA')
        cam.prop(user, "bool_point_cloud")
        cam.prop(user, "bool_reference_point")
        self.layout.split(factor=0.0, align=False)

    def face_layout(self, user):
        # face tracking data options
        face = self.layout.box()
        face.label(text="Face Track Import Options") # , icon='MESH_DATA')
        face.prop(user, "enum_face_type")
        self.layout.split(factor=2.0, align=False)

    def import_btn(self, user):
        # import button
        btn_txt = user.button_import_text
        self.layout.operator("button.import_tracking_data", text=btn_txt)