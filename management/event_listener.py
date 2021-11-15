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

from management import execution_manager
from utils import pathing
from setup import compositing


def file_to_load(m_path):
    # todo: implement event struct
    print("\n" + "processing input path:", m_path)
    paths, valid = pathing.process_path(m_path)
    if valid:
        manager = execution_manager.ExecutionManager()
        manager.import_models(paths)
    print("\n" + "file imported")


def internal_compositing():
    tree = compositing.CompositingTree()
    compositing.set_internal_compositing(tree)
    compositing.setup_render()
    print("set internal compositing")


def external_compositing():
    tree = compositing.CompositingTree()
    compositing.set_external_compositing(tree)
    compositing.setup_render()
    print("set external compositing")


"""
# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-03-12_00-29-55_cam.zip"
file_to_load(manual_file)
"""


