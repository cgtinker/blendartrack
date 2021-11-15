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

    button_copy_rig: StringProperty(
        name="",
        description="",
        default="Copy Driver Motion to Face"
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
    rig_mouth_influence: FloatProperty(
        name="mouth influence",
        description="",
        min=0,
        max=1.0,
        default=0.5,
    )

    rig_mouth_influence: FloatProperty(
        name="mouth influence",
        description="",
        min=0,
        max=1.0,
        default=0.5,
    )

    rig_brow_influence: FloatProperty(
            name="brow influence",
            description="",
            min=0,
            max=1.0,
            default=0.5,
        )

    rig_eye_influence: FloatProperty(
            name="eye influence",
            description="",
            min=0,
            max=1.0,
            default=0.5,
        )

    rig_cheek_influence: FloatProperty(
        name="cheek influence",
        description="",
        min=0,
        max=1.0,
        default=0.5,
    )

    rig_chin_influence: FloatProperty(
        name="chin influence",
        description="",
        min=0,
        max=1.0,
        default=0.5,
    )


def get_user():
    return bpy.context.scene.m_cgtinker_blendartrack
