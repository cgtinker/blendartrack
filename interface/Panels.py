from bpy.types import Panel
import bpy


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
        self.path_prop_layout(user)
        self.draw_camera_layout(user)

        #self.import_button(user)

    def path_prop_layout(self, user):
        # self.layout.label(text="import .zip blendartrack data")
        self.layout.prop(user, "data_path")
        self.layout.split(factor=1.0, align=False)

    def draw_camera_layout(self, user):
        cam = self.layout.box()
        cam.label(text="Camera Track Import Options")  # , icon='EMPTY_DATA')

        row_a = cam.row()
        row_a.prop(user, "bool_point_cloud")
        row_a.prop(user, "bool_reference_point")

        self.layout.split(factor=2.0, align=False)


    def import_button(self, user):
        self.layout.operator("button.import_tracking_data", text=user.button_import_text)


class UI_PT_camera_panel(DefaultPanel, Panel):
    bl_label = "compositing"
    bl_idname = "OBJECT_PT_camera_panel"
    #bl_parent_id = "OBJECT_PT_parent_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        # self.layout.label(text="This is my first child")

        self.camera_layout(user)

    def camera_layout(self, user):

        compositing = self.layout.box()
        compositing.label(text="Setup Compositing")  # , icon='EMPTY_DATA')
        row_b = compositing.row()
        row_b.operator("button.internal_compositing", text=user.button_internal_compositing)
        row_b.operator("button.external_compositing", text=user.button_external_compositing)
        self.layout.split(factor=0.0, align=False)


class UI_PT_main_panel_extension(DefaultPanel, Panel):
    bl_label = "none"
    bl_idname = "OBJECT_PT_main_panel_extension"
    bl_options = {"HIDE_HEADER"}

    def draw(self, context):

        user = context.scene.m_cgtinker_blendartrack

        self.face_layout(user)

    def face_layout(self, user):
        # face tracking data options
        face = self.layout.box()
        face.label(text="face track import options")  # , icon='MESH_DATA')
        face.prop(user, "enum_face_type")
        self.layout.split(factor=2.0, align=False)


class UI_PT_face_panel(DefaultPanel, Panel):
    bl_label = "face rigging"
    bl_idname = "OBJECT_PT_face_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        layout = self.layout




class UI_PT_face_rigging_panel(DefaultPanel, Panel):
    bl_label = "android rigging preview"
    # bl_idname = "OBJECT_PT_face_rigging"
    bl_parent_id = "OBJECT_PT_face_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        self.rigging_layout(user)

    def rigging_layout(self, user):
        base = self.layout.box()
        base.label(text="Requires one collection of animated empties")
        base.operator("button.base_rig", text=user.button_base_rig)

        self.layout.split(factor=2.0, align=False)

        weight = self.layout.box()
        weight.label(text="Facial Motions")
        weight.prop(user, 'rig_mouth_influence', slider=True)
        weight.prop(user, 'rig_brow_influence', slider=True)
        weight.prop(user, 'rig_eye_influence', slider=True)
        weight.prop(user, 'rig_cheek_influence', slider=True)
        weight.prop(user, 'rig_chin_influence', slider=True)

        weight.split(factor=1.0, align=False)
        weight.operator("button.driver_rig", text=user.button_driver_rig)

        self.layout.split(factor=2.0, align=False)

        copy = self.layout.box()
        copy.label(text="Requires Rigify Super Face")
        copy.operator("button.copy_rig", text=user.button_copy_rig)
