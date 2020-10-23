import json
import codecs
print("wtf03")

import bpy
import os
import sys

print("wtf03")
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

print(blend_dir)

from main import jsonDecoder as jd 
from main import keyframeAssistent as ka

#accessing json data
jsonPath = "/Users/Scylla/Downloads/CameraPose.json"
jsonData = json.load(codecs.open(jsonPath, 'r', 'utf-8-sig'))

class poseData:
    def __init__(self, px, py, pz, rx, ry, rz, frame):
        #assign pos
        self.px = px
        self.py = py
        self.pz = pz
        #assign rotation_euler
        self.rx = rx
        self.ry = ry
        self.rz = rz
        #assign frame
        self.frame = frame

    def initFrame(self, scene, obj):
        ka.InitKeyframe(self.frame, scene, obj)

    def keyPos(self, obj):
        ka.PosKeyframes(self.px, self.py, self.pz, obj)

    def keyRot(self, obj):
        ka.RotKeyframes(self.rx, self.ry, self.rz, obj)

    def printContents(self):
        print('px', self.px, 'py', self.py, 'pz', self.pz, 'rx', self.rx, 'ry', self.ry, 'rz', self.rz, 'f', self.frame)

def initPoseList(jsonData):
    #store pose data
    global poseList
    poseList = []
    #decoding json
    for data in jsonData['poseList']:
        px, py, pz = jd.SplitPosData(data)
        rx, ry, rz = jd.SplitRotData(data)
        frame = (data['frame'])
        #append data to list
        obj = poseData(px, py, pz, rx, ry, rz, frame)
        poseList.append(obj)

initPoseList(jsonData)

for data in poseList:
    data.printContents()
