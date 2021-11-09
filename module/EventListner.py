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
from .execution import ExecutionHandler, ExecutionManager
from .preperation.queue import QueueManager
from .preperation.importing import InitDataTypes
from .preperation.pathing import Pathing
import importlib

importlib.reload(InitDataTypes)
importlib.reload(ExecutionHandler)
importlib.reload(Pathing)
importlib.reload(QueueManager)


def file_to_load(m_path):
    print("\n"+"processing input path:", m_path)
    paths, valid = Pathing.process_path(m_path)
    print("")

    if valid:
        files_in_queue = QueueManager.get_valid_files(paths)
        print("")
        manager = ExecutionManager.ExecutionManager(files_in_queue)
        manager.execute_queue()

    else:
        print("given path isn't valid")

    print("\n"+"\n"+"finished processing" + "\n")


from management import queue, execution_manager


def manual_test_loader(m_path):
    print("\n" + "processing input path:", m_path)
    paths, valid = Pathing.process_path(m_path)
    print("")

    if valid:
        queue_manager = queue.QueueManager(paths)
        manager = execution_manager.ExecutionManager(queue_manager.staged_files)
        pass


"""
# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-03-12_00-29-55_cam.zip"
file_to_load(manual_file)
"""


