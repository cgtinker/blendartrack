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

from main.common import jsonValidator as jV
import dataImportManager as dIM

# path to json file
global JSON_PATH
JSON_PATH = "/Users/Scylla/Downloads/CameraPose.json"


def none(CUR_DATA):
    print("none")


def exec_pose_data(CUR_DATA):
    for data in CUR_DATA:
        data.print_content()


def exec_face_mesh(CUR_DATA):
    print("face_mesh")


def exec_shape_keys(CUR_DATA):
    print("keys")


exe_data = {
    0: none,
    1: exec_pose_data,
    2: exec_face_mesh,
    3: exec_shape_keys
}


def execute_data(CUR_TYPE, CUR_DATA):
    # get the function by a (int) current type
    func = exe_data.get(CUR_TYPE, CUR_DATA)
    # create a reference of the current data
    func(CUR_DATA)

# validating json
JSON_DATA = jV.start_validation(JSON_PATH)
# get json data type
CUR_TYPE = dIM.json_data_type(JSON_DATA)
# get processed data ready for execution
CUR_DATA = dIM.return_received_data(CUR_TYPE, JSON_DATA)
# execute processed data
execute_data(CUR_TYPE, CUR_DATA)

print("finished processing")
