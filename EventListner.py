import os
import sys
import bpy

# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)

from main import JsonDataImporter, ExecuteModel
import importlib

importlib.reload(JsonDataImporter)
importlib.reload(ExecuteModel)

# ---------------------------------------------------------------------------------------------
# set path to json file

# path = "/Users/Scylla/Downloads/20201113_145709_BS.json"
path = "/Users/Scylla/Downloads/FaceMeshData-1.json"
# path = "/Users/Scylla/Downloads/CameraPose-1.json"
# ---------------------------------------------------------------------------------------------

# importing json data and execute it
JsonDataImporter.import_json_data(path)

print("finished processing")
