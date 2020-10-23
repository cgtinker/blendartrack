import bpy
import json
import os 
import codecs
import PathHandler

jsonPath = "/Users/Scylla/Downloads/CameraPose.json"

# accessing json data, adding utf-8 bom header
data = json.load(codecs.open(jsonPath, 'r', 'utf-8-sig'))
#print(data)

#pi is not defined
pi = 3.14159265

#getting scene ref & adjusting scene frame end
scene = bpy.context.scene
len = len(data['poseList'])
if scene.frame_end < len:
    scene.frame_end = len
   
    
#adding empty camera
def addActiveCamera():
    bpy.ops.object.camera_add()
    activeCamera = bpy.data.objects['Camera']
    activeCamera.name = 'activeCamera'    

def getSelectedObject():
    objs = len(bpy.context.selected_objects)
    print("count: ", objs)
    if objs > 0:
        print("hi")
    else:
        addActiveCamera()
    
def SplitPosData(posData):
    px = (cameraPose['pos']['x'])
    py = (cameraPose['pos']['y'])
    pz = (cameraPose['pos']['z'])
    return(px, py, pz)

def SplitRotData(rotData):
    rx = (cameraPose['rot']['x'])
    ry = (cameraPose['rot']['y'])
    rz = (cameraPose['rot']['z'])
    return(rx, ry, rz)

def InitKeyframe(scene, obj, f):
    #select object for keyframing
    object = obj
    bpy.context.scene.frame_set(f) 

def PosKeyframes(px, py, pz):
    #set camera translation
    camera.location.x = px;
    camera.location.y = py;
    camera.location.z = pz;   
    #set translation keyframe
    camera.keyframe_insert(data_path="location")

def RotKeyframes(rx, ry, rz):
    camera.rotation_mode = 'XYZ'
    camera.rotation_euler[0] = rx*(pi/180.0)
    camera.rotation_euler[1] = ry*(pi/180.0)
    camera.rotation_euler[2] = rz*(pi/180.0)
    #set rotation keyframe
    camera.keyframe_insert("rotation_euler")


#getSelectedObject()
addActiveCamera()
camera = bpy.data.objects['activeCamera']

#setting camera keyframes
for cameraPose in data['poseList']:
    px, py, pz = SplitPosData(cameraPose)
    rx, ry, rz = SplitRotData(cameraPose)  
    f = (cameraPose['frame'])
    
    InitKeyframe(scene, camera, f)
    PosKeyframes(px, py, pz)
    RotKeyframes(rx, ry, rz)
    #setupCamera(scene, px, py, pz, rx, ry, rz, f) 
    
    
print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
