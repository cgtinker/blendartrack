import json
import codecs
import bpy
import os
import sys

#getting access to the current dir
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

#print("dir: ", blend_dir)
from main import poseDataHandler as pdh

#path to json file
jsonPath = "/Users/Scylla/Downloads/CameraPose.json"

jsonTypes = {
    "none": 0,
    "poseList": 1,
    "faceList": 2, 
    "otherList": 3
    }

#validation of the incomming json
def validateJSON(jsonData):
    try:
        jsonData = json.load(codecs.open(jsonPath, 'r', 'utf-8-sig'))
    except ValueError as err:
        return False
    return True

#analyzing the json data type
def getJsonType(jsonData):
    for data in jsonTypes:        
        if data in jsonData:
            global curType
            curType = jsonTypes[data]
            print("data type: ", data, curType)

def startValidation():
    if validateJSON(jsonPath):
        jsonData = json.load(codecs.open(jsonPath, 'r', 'utf-8-sig'))
        getJsonType(jsonData)

    else:
        print("given json is not valid")

def startImportProcess():
    print("start importing: ", curType)
    
startValidation()
startImportProcess()

def importPoseData():
    pdh.initPoseList(jsonData)

    for data in pdh.poseList:
        data.printContents()
#print("testing validation: ", jsonData["poseList"])
