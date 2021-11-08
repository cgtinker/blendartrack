'''
Copyright (C) cgtinker, cgtinker.com, hello@cgtinker.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "blendartrack",
    "description": "Blendartrack motion tracking data import add-on",
    "author": "cgtinker",
    "version": (0, 6, 0),
    "blender": (2, 90, 0),
    "location": "3D View > Tool",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import importlib
import os
import sys

# append sys path to dir
main_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'module')
sys.path.append(main_dir)

# import interface
from .module.bpy_bridge.interface import Panels, Properties, Operators, Registration

importlib.reload(Operators)
importlib.reload(Panels)
importlib.reload(Properties)

classes = (
    Properties.MyProperties,
    Operators.UI_import_button,
    Panels.UI_main_panel
)


def register():
    Registration.register(classes, Properties.MyProperties)


def unregister():
    Registration.unregister(classes)


if __name__ == "__main__":
    register()
