import os
from pathlib import Path
"""
# for manual debugging
import bpy
import sys
# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)
"""
from module import ImportJson, ExecuteModel, Pathing, Queue
import importlib

importlib.reload(ImportJson)
importlib.reload(ExecuteModel)
importlib.reload(Pathing)
importlib.reload(Queue)


def file_to_load(m_path):
    print("loading")
    paths, valid = Pathing.process_path(m_path)
    if valid:
        Queue.queue_files(paths)
    else:
        print("given path isn't valid")


# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-01-05_16-54-42_face/2021-01-05_16-54-42_face.json"
file_to_load(manual_file)


print("finished processing")
