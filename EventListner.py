import os
from pathlib import Path
"""
# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)
"""
from .module import JsonDataImporter, ExecuteModel
import importlib

importlib.reload(JsonDataImporter)
importlib.reload(ExecuteModel)


def ImportJsonData(path):
    JsonDataImporter.import_json_data(path)


def filetoload(path):
    print(path, "loading el")

    if os.path.isabs(path):
        m_path = Path(path).resolve()
        ImportJsonData(m_path)

    else:
        m_path = Path(os.path.abspath(path)).resolve()
        ImportJsonData(m_path)


print("finished processing")
