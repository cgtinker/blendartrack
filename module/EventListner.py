"""
# for manual debugging
import bpy
import sys
import os
# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)
"""
from module.execution import ExecutionHandler, ExecutionManager
from module.preperation.queue import QueueManager
from module.preperation.importing import InitDataTypes
from module.preperation.pathing import Pathing
import importlib

importlib.reload(InitDataTypes)
importlib.reload(ExecutionHandler)
importlib.reload(Pathing)
importlib.reload(QueueManager)


def file_to_load(m_path):
    print("processing input path")
    print("path:", m_path)
    paths, valid = Pathing.process_path(m_path)
    if valid:
        files_in_queue = QueueManager.get_valid_files(paths)
        ExecutionManager.execute_queue(files_in_queue)
    else:
        print("given path isn't valid")


"""
# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-03-12_00-29-55_cam.zip"
file_to_load(manual_file)
"""

print("")
print("finished processing")
