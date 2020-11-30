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
from .module import JsonDataImporter, ExecuteModel
import importlib

importlib.reload(JsonDataImporter)
importlib.reload(ExecuteModel)


def import_json_data(normalized_path):
    JsonDataImporter.import_json_data(normalized_path)


def file_to_load(json_path):
    print(json_path, "loading el")

    if os.path.isabs(json_path):
        m_path = Path(json_path).resolve()
        import_json_data(m_path)

    else:
        m_path = Path(os.path.abspath(json_path)).resolve()
        import_json_data(m_path)


# for manual debugging
# manual_path = "/Users/Scylla/Desktop/resolveIntrinsics/20201127_165204_CI.json"
# file_to_load(manual_path)


print("finished processing")
