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

from management import queue, task_allocator, execution_manager
from utils import pathing


def file_to_load(m_path):
    print("\n" + "processing input path:", m_path)
    paths, valid = pathing.process_path(m_path)
    print("")

    if valid:
        queue_manager = queue.QueueManager(paths)
        allocator = task_allocator.TaskAllocator(queue_manager.staged_files)
        manager = execution_manager(allocator.staged_models)
        pass


"""
# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-03-12_00-29-55_cam.zip"
file_to_load(manual_file)
"""


