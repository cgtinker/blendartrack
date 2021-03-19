"""
This file should be loaded in a .blend file which should be located in the _retargeting folder.
It's included for manual debugging
"""

import os
import bpy
import sys

from module.execution import ExecutionHandler
from module.preperation.queue import QueueManager
from module.preperation.importing import InitDataTypes
from module.preperation.pathing import Pathing
import importlib
importlib.reload(InitDataTypes)
importlib.reload(ExecutionHandler)
importlib.reload(Pathing)
importlib.reload(QueueManager)

# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)


def file_to_load(m_path):
    print("loading")
    paths, valid = Pathing.process_path(m_path)
    if valid:
        QueueManager.get_valid_files(paths)
    else:
        print("given path isn't valid")


# paths for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-01-08_21-43-39/2021-01-08_14-21-58_cam.zip"
file_to_load(manual_file)


print("finished processing")
