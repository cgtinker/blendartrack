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
<<<<<<< HEAD
        self.draw_path_prop_layout(user)
        self.draw_camera_import(user)
        self.draw_face_import(user)
        self.draw_import_button(user)

    def draw_path_prop_layout(self, user):
        self.layout.prop(user, "data_path")
        self.layout.split(factor=1.0, align=False)

    def draw_camera_import(self, user):
=======
        self.path_prop_layout(user)
        self.draw_camera_layout(user)

        #self.import_button(user)

    def path_prop_layout(self, user):
        # self.layout.label(text="import .zip blendartrack data")
        self.layout.prop(user, "data_path")
        self.layout.split(factor=1.0, align=False)

    def draw_camera_layout(self, user):
>>>>>>> 03cdd482d47a39126b818d7f0ab697862a41436d
        cam = self.layout.box()
        cam.label(text="Camera Track Import Options")  # , icon='EMPTY_DATA')

        row_a = cam.row()
        row_a.prop(user, "bool_point_cloud")
        row_a.prop(user, "bool_reference_point")

        self.layout.split(factor=2.0, align=False)
<<<<<<< HEAD
=======


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
>>>>>>> 03cdd482d47a39126b818d7f0ab697862a41436d

    def draw_face_import(self, user):
        # face tracking data options
        face = self.layout.box()
        face.label(text="face track import options")  # , icon='MESH_DATA')
        face.prop(user, "enum_face_type")
        self.layout.split(factor=2.0, align=False)

    def draw_import_button(self, user):
        # import button
        self.layout.operator("button.import_tracking_data", text=user.button_import_text)


<<<<<<< HEAD
class UI_PT_compositing_panel(DefaultPanel, Panel):
    bl_label = "compositing"
    bl_idname = "OBJECT_PT_compositing_panel"
=======
class UI_PT_main_panel_extension(DefaultPanel, Panel):
    bl_label = "none"
    bl_idname = "OBJECT_PT_main_panel_extension"
    bl_options = {"HIDE_HEADER"}
>>>>>>> 03cdd482d47a39126b818d7f0ab697862a41436d

    def draw(self, context):

        user = context.scene.m_cgtinker_blendartrack
<<<<<<< HEAD
        self.draw_camera_layout(user)

    def draw_camera_layout(self, user):
        compositing = self.layout.box()
        compositing.label(text="Setup Compositing")  # , icon='EMPTY_DATA')
        row_b = compositing.row()
        row_b.operator("button.internal_compositing", text=user.button_internal_compositing)
        row_b.operator("button.external_compositing", text=user.button_external_compositing)
        self.layout.split(factor=0.0, align=False)
=======

        self.face_layout(user)

    def face_layout(self, user):
        # face tracking data options
        face = self.layout.box()
        face.label(text="face track import options")  # , icon='MESH_DATA')
        face.prop(user, "enum_face_type")
        self.layout.split(factor=2.0, align=False)
>>>>>>> 03cdd482d47a39126b818d7f0ab697862a41436d


class UI_PT_face_panel(DefaultPanel, Panel):
    bl_label = "face rigging"
    bl_idname = "OBJECT_PT_face_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        layout = self.layout




class UI_PT_face_rigging_panel(DefaultPanel, Panel):
    bl_label = "android face rigging preview"
    bl_idname = "OBJECT_PT_rigging_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        self.draw_rigging_layout(user)

    def draw_rigging_layout(self, user):
        base = self.layout.box()
        base.label(text="Rig to Animated Empties")
        base.operator("button.face_rig", text=user.button_base_rig)

        self.layout.split(factor=2.0, align=False)
        weight = self.layout.box()
<<<<<<< HEAD
        weight.label(text="Driver Rig Motion Influence")
        weight.prop(user, 'jaw_master_influence', slider=True)
        weight.prop(user, 'jaw_sides_influence', slider=True)
        weight.prop(user, 'chin_master_influence', slider=True)
        weight.prop(user, 'chin_sides_influence', slider=True)
        weight.prop(user, 'lips_influence', slider=True)
        weight.prop(user, 'lid_influence', slider=True)
        weight.prop(user, 'brow_master_influence', slider=True)
        weight.prop(user, 'brow_sides_influence', slider=True)
        weight.prop(user, 'nose_influence', slider=True)

        weight.split(factor=2.0, align=False)
=======
        weight.label(text="Facial Motions")
        weight.prop(user, 'rig_mouth_influence', slider=True)
        weight.prop(user, 'rig_brow_influence', slider=True)
        weight.prop(user, 'rig_eye_influence', slider=True)
        weight.prop(user, 'rig_cheek_influence', slider=True)
        weight.prop(user, 'rig_chin_influence', slider=True)

        weight.split(factor=1.0, align=False)
>>>>>>> 03cdd482d47a39126b818d7f0ab697862a41436d
        weight.operator("button.driver_rig", text=user.button_driver_rig)

        self.layout.split(factor=2.0, align=False)
        copy = self.layout.box()
        copy.label(text="Driver Motion to Rigify Face")
        copy.operator("button.copy_rig", text="Copy Drive Motion To Rig")

