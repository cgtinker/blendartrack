from bpy.types import Panel


class DefaultPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "blendartrack"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return (context.object is not None)


class UI_PT_main_panel(DefaultPanel, Panel):
    bl_label = "blendartrack"
    bl_idname = "OBJECT_PT_parent_panel"
    bl_options = {"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack

        # draw layout
        self.draw_path_prop_layout(user)
        self.draw_camera_layout(user)
        self.import_button(user)

    def draw_path_prop_layout(self, user):
        self.layout.prop(user, "data_path")
        self.layout.split(factor=1.0, align=False)

    def draw_camera_layout(self, user):
        cam = self.layout.box()
        cam.label(text="Camera Track Import Options")  # , icon='EMPTY_DATA')

        row_a = cam.row()
        row_a.prop(user, "bool_point_cloud")
        row_a.prop(user, "bool_reference_point")

        self.layout.split(factor=2.0, align=False)

