from bpy.types import Panel


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
        btn_txt = cgtinker_blendartrack.button_import_text
        layout.operator("button.import_tracking_data", text = btn_txt)