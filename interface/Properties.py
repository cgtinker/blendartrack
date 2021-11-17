import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, FloatProperty
from bpy.types import PropertyGroup


class MyProperties(PropertyGroup):
    # PATHS
    data_path: StringProperty(
        name="File Path",
        description="File path to .zip or .json file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

    # BUTTONS
    button_import_text: StringProperty(
        name="",
        description="Import Tracking data from file path",
        default="Import Data"
    )

    button_internal_compositing: StringProperty(
        name="",
        description="",
        default="Internal"
    )

    button_external_compositing: StringProperty(
        name="",
        description="",
        default="External"
    )

    button_base_rig: StringProperty(
        name="",
        description="",
        default="Generate Face Rig"
    )

    button_driver_rig: StringProperty(
        name="",
        description="",
        default="Generate Driver Rig"
    )

    button_driver_update: StringProperty(
        name="",
        description="",
        default="Update Driver Influence"
    )

    button_copy_rig: StringProperty(
        name="",
        description="",
        default="Bake To Action"
    )

    # BOOLS
    bool_point_cloud: BoolProperty(
        name="Point Cloud",
        description="Dots recognized during the tracking process",
        default=True
    )

    bool_reference_point: BoolProperty(
        name="Reference Points",
        description="Reference points placed during the tracking process",
        default=True
    )

    # ENUMS
    enum_face_type: EnumProperty(
        name="",
        description="Either import an animated face mesh or animated empties",
        items=[('MESH', "Face Mesh", "Import an animated face mesh"),
               ('EMPTIES', "Animated Empties", "Import animated empties")]
    )

    # SLIDER
    jaw_master_influence: FloatProperty(
        name="jaw master influence",
        description="",
        min=0,
        max=1.0,
        default=1,
    )

    jaw_sides_influence: FloatProperty(
        name="jaw sides influence",
        description="",
        min=0,
        max=1.0,
        default=0.25,
    )

    chin_master_influence: FloatProperty(
        name="chin master influence",
        description="",
        min=0,
        max=1.0,
        default=1.
    )

    chin_sides_influence: FloatProperty(
        name="chin sides influence",
        description="",
        min=0,
        max=1.0,
        default=0.75,
    )

    lips_influence: FloatProperty(
        name="lips influence",
        description="",
        min=0,
        max=1.0,
        default=1,
    )

    lid_influence: FloatProperty(
        name="lid influence",
        description="",
        min=0,
        max=1.0,
        default=0.75,
    )

    brow_master_influence: FloatProperty(
        name="brow master influence",
        description="",
        min=0,
        max=1.0,
        default=0.75,
    )

    brow_sides_influence: FloatProperty(
        name="brow sides influence",
        description="",
        min=0,
        max=1.0,
        default=0.25,
    )

    nose_influence: FloatProperty(
        name="nose influence",
        description="",
        min=0,
        max=1.0,
        default=0.5,
)


def get_user():
    return bpy.context.scene.m_cgtinker_blendartrack
