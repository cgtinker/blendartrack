import json
import codecs
#
import jsonDecoder as jd
import keyframeAssistent as ka

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
        print(self.px, self.py, self.pz, self.rx, self.ry, self.rz, self.frame)

def initPoseList():
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

initPoseList()

for data in poseList:
    data.printContents()
