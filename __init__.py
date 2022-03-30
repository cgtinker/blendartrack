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
    "name":        "BlendArTrack",
    "description": "BlendArTrack - motion tracking data import add-on",
    "author":      "cgtinker",
    "version":     (2, 1, 0),
    "blender":     (2, 90, 0),
    "location":    "3D View > Tool",
    "warning":     "",
    "wiki_url":    "",
    "tracker_url": "",
    "category":    "Development"
}

import importlib

"""
import os
import sys
import bpy
# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)

# append sys path to dir
main_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'module')
sys.path.append(main_dir)
"""

from .src.interface import cgt_registration
#
# importlib.reload(Properties)
# importlib.reload(Registration)


def reload_modules():
    from .src import cgt_imports
    cgt_imports.manage_imports(True)


if "bl_info" in locals():
    reload_modules()


def register():
    cgt_registration.register()


def unregister():
    cgt_registration.unregister()


if __name__ == "__main__":
    register()
