"""
import os
import sys
import bpy

#getting access to the current dir
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

print("dir: ", blend_dir)
"""

from main import dataTypeAnalyser as dta

# path to json file
global jsonPath
jsonPath = "/Users/Scylla/Downloads/CameraPose.json"

dta.start_validation(jsonPath)

dta.start_import_process()
print("finished processing")