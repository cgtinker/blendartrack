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
from .module import ImportJson, ExecuteModel, Pathing, Queue
import importlib

importlib.reload(ImportJson)
importlib.reload(ExecuteModel)
importlib.reload(Pathing)
importlib.reload(Queue)

'''
def import_json_data(normalized_path):
    ImportJson.import_json_data(normalized_path)


def file_to_load(json_path):
    print("start to load", json_path)

    if os.path.isabs(json_path):
        m_path = Path(json_path).resolve()
        import_json_data(m_path)

    else:
        m_path = Path(os.path.abspath(json_path)).resolve()
        import_json_data(m_path)
'''


def file_to_load(m_path):
    print("loading")
    paths, valid = Pathing.process_path(m_path)
    if valid:
        Queue.queue_files(paths)
    else:
        print("given path isn't valid")


'''
# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2020-12-17_14-45-01_cam"
manual_file = "/Users/Scylla/Downloads/2020-12-17_14-45-01_cam/2020-12-17_14-45-01_anchor.json"
load_data(file_to_load)
'''

print("finished processing")
