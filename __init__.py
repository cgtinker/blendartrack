bl_info = {
    "name": "retargeting",
    "description": "",
    "author": "cgtinker",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "3D View > Tool",
    "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

import os
import sys

#
# blend_dir = os.path.dirname(bpy.data.filepath)
# if blend_dir not in sys.path:
#   sys.path.append(blend_dir)
# temporarily appends the folder containing this file into sys.path

main_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'module')
sys.path.append(main_dir)

from . import EventListner
import importlib

importlib.reload(EventListner)

# ------------------------------------------------------------------------
#    FileBrowser
# ------------------------------------------------------------------------

public_filename = ""


class OpenFilebrowser(Operator, ImportHelper):
    bl_idname = "open_filebrowser"
    bl_label = "Open the file browser"

    filter_glob: StringProperty(
        default='*.json',
        options={'HIDDEN'}
    )

    some_boolean: BoolProperty(
        name='Do a thing',
        description='Do a thing with the file you\'ve selected',
        default=True,
    )

    def execute(self, context):
        """Do something with the selected file(s)."""
        filename, extension = os.path.splitext(self.filepath)
        print('Selected file:', self.filepath)
        print('File name:', filename)
        print('File extension:', extension)
        print('Some Boolean:', self.some_boolean)
        return {'FINISHED'}

    # ------------------------------------------------------------------------


#    Scene Properties
# ------------------------------------------------------------------------

class MyProperties(PropertyGroup):
    """
    my_bool: BoolProperty(
        name="Enable or Disable",
        description="A bool property",
        default = False
        )

    my_int: IntProperty(
        name = "Int Value",
        description="A integer property",
        default = 23,
        min = 10,
        max = 100
        )

    my_float: FloatProperty(
        name = "Float Value",
        description = "A float property",
        default = 23.7,
        min = 0.01,
        max = 30.0
        )

    my_float_vector: FloatVectorProperty(
        name = "Float Vector Value",
        description="Something",
        default=(0.0, 0.0, 0.0),
        min= 0.0, # float
        max = 0.1
    )

    my_string: StringProperty(
        name="User Input",
        description=":",
        default="",
        maxlen=1024,
        )
    """
    my_path: StringProperty(
        name="Directory",
        description="Choose a directory:",
        default="",
        # maxlen=1024,
        subtype='FILE_PATH'
    )
    """
    my_enum: EnumProperty(
        name="Dropdown:",
        description="Apply Data to attribute.",
        items=[ ('OP1', "Option 1", ""),
                ('OP2', "Option 2", ""),
                ('OP3', "Option 3", ""),
               ]
        )
    """


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class WM_OT_HelloWorld(Operator):
    bl_label = "Start Retargeting"
    bl_idname = "wm.hello_world"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        EventListner.filetoload(mytool.my_path)

        # print the values to the console
        """
        print("Hello World")
        print("bool state:", mytool.my_bool)
        print("int value:", mytool.my_int)
        print("float value:", mytool.my_float)
        print("string value:", mytool.my_string)   

        public_filename = mytool.my_path
        print("string value:", mytool.my_path)


        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        filename = path + "/EventListner.py"
        exec(compile(open(filename) .read(), filename, 'exec'))  



        print("enum state:", mytool.my_enum)
        """
        return {'FINISHED'}


# ------------------------------------------------------------------------
#    Menus
# ------------------------------------------------------------------------

class OBJECT_MT_CustomMenu(bpy.types.Menu):
    bl_label = "Select"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout

        # Built-in operators
        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class OBJECT_PT_CustomPanel(Panel):
    bl_label = "Retargeting Crossplatform"  # name in panel
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Retargeter"  # displayed name
    bl_context = "objectmode"

    """
    @classmethod
    def poll(self,context):
        return context.object is not None
    """

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        """
        layout.prop(mytool, "my_bool")
        layout.prop(mytool, "my_enum", text="") 
        layout.prop(mytool, "my_int")
        layout.prop(mytool, "my_float")
        layout.prop(mytool, "my_float_vector", text="")
        layout.prop(mytool, "my_string")
        """
        layout.prop(mytool, "my_path")
        layout.operator("wm.hello_world")
        """
        layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()
        """


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    MyProperties,
    WM_OT_HelloWorld,
    OBJECT_MT_CustomMenu,
    OBJECT_PT_CustomPanel
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    print("Hello World")
    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
