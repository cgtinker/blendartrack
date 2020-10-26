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

from main import jsonValidator as jV, jsonDataImport as dIM

# path to json file
json_path = "/Users/Scylla/Downloads/CameraPose.json"


def none():
    print("none")


def exec_pose_data(cur_data):
    for data in cur_data:
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


def execute_data(cur_type, cur_data):
    # get the function by a (int) current type
    func = exe_data.get(cur_type, cur_data)
    # create a reference of the current data
    func(cur_data)


received_data = dIM.import_valid_json(json_path)
# validating json
# json_data = jV.start_validation(json_path)
# import json data
# received_data = dIM.import_json_data(json_data)
# execute data
execute_data(1, received_data)

print("finished processing")
