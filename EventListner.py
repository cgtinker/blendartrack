"""
import os
import sys
import bpy

#getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

print("dir: ", blend_dir)
"""

from main import JsonImporter
from main import ModelRunner

# path to json file
json_path = "/Users/Scylla/Downloads/CameraPose.json"


model_data = JsonImporter.import_json_data(json_path)

print("finished processing")
