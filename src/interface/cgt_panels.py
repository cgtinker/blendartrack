from bpy.types import Panel


class DefaultPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlendAR"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}


class ExpandedPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlendAR"
    bl_context = "objectmode"
    bl_options = {"HEADER_LAYOUT_EXPAND"}


class UI_PT_main_panel(DefaultPanel, Panel):
    bl_label = "BlendArTrack"
    bl_idname = "OBJECT_PT_parent_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack

        # draw layout
        self.draw_path_prop_layout(user)
        self.draw_camera_import(user)
        self.draw_face_import(user)
        self.draw_import_button(user)

    def draw_path_prop_layout(self, user):
        self.layout.prop(user, "data_path")
        self.layout.split(factor=1.0, align=False)

    def draw_camera_import(self, user):
        cam = self.layout.box()
        cam.label(text="Camera Import Options")  # , icon='EMPTY_DATA')

        row_a = cam.row()
        row_a.prop(user, "bool_point_cloud")
        row_a.prop(user, "bool_reference_point")

        self.layout.split(factor=2.0, align=False)

    def draw_face_import(self, user):
        # face tracking data options
        face = self.layout.box()
        face.label(text="Face Import Options")  # , icon='MESH_DATA')
        face.prop(user, "enum_face_type", expand=True, text="face import opt")
        self.layout.split(factor=2.0, align=False)

    def draw_import_button(self, user):
        # import button
        self.layout.operator("button.import_tracking_data", text=user.button_import_text)


class UI_PT_compositing_panel(DefaultPanel, Panel):
    bl_label = "Compositing"
    bl_parent_id = "OBJECT_PT_parent_panel"
    # bl_idname = "OBJECT_PT_compositing_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        self.draw_camera_layout(user)

    def draw_camera_layout(self, user):
        compositing = self.layout.box()
        compositing.label(text="Setup Compositing")  # , icon='EMPTY_DATA')
        row_b = compositing.row()
        row_b.operator("button.internal_compositing", text=user.button_internal_compositing)
        row_b.operator("button.external_compositing", text=user.button_external_compositing)
        self.layout.split(factor=0.0, align=False)


class UI_PT_face_rigging_panel(DefaultPanel, Panel):
    bl_label = "Face Rigging"
    bl_parent_id = "OBJECT_PT_parent_panel"
    # bl_idname = "OBJECT_PT_rigging_panel"

    def draw(self, context):
        user = context.scene.m_cgtinker_blendartrack
        self.draw_layout(user)

    def draw_layout(self, user):
        device = self.layout.box()
        device.label(text="Input Device Type")  # , icon='MESH_DATA')
        device.prop(user, "enum_device_type", expand=True, text="input device")
        self.layout.split(factor=2.0, align=False)

        base = self.layout.box()
        base.label(text="Rig to Animated Empties")
        base.operator("button.face_rig", text=user.button_base_rig)

        self.layout.split(factor=2.0, align=False)
        weight = self.layout.box()
        weight.label(text="Driver Rig")
        weight.operator("button.driver_rig", text=user.button_driver_rig)

        weight.split(factor=4.0, align=False)
        weight.prop(user, 'jaw_master_influence', slider=True)
        weight.prop(user, 'jaw_sides_influence', slider=True)
        weight.prop(user, 'chin_master_influence', slider=True)
        weight.prop(user, 'chin_sides_influence', slider=True)
        weight.prop(user, 'lips_influence', slider=True)
        weight.prop(user, 'lid_influence', slider=True)
        weight.prop(user, 'brow_master_influence', slider=True)
        weight.prop(user, 'brow_sides_influence', slider=True)
        weight.prop(user, 'nose_influence', slider=True)

        # weight.split(factor=2.0, align=False)
        weight.operator("button.driver_update", text=user.button_driver_update)

        self.layout.split(factor=2.0, align=False)
        copy = self.layout.box()
        copy.label(text="Transfer Motion")
        copy.operator("button.copy_rig", text=user.button_copy_rig)



