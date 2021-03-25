from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import PropertyGroup


class MyProperties(PropertyGroup):
    data_path: StringProperty(
        name="File Path",
        description="File path to .zip or .json file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

    button_import_text: StringProperty(
        name="",
        description="Button Display Text",
        default="Import Data"
    )

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

    enum_face_type: EnumProperty(
        name="",
        description="Either import an animated face mesh or animated empties",
        items=[('MESH', "Face Mesh", "Import an animated face mesh"),
               ('EMPTIES', "Animated Empties", "Import animated empties")]
    )