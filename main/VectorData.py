import bpy
import json
import os 

#pi is not defined
pi = 3.14159265

#reformatting json vector
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

#preparing to keyframe
def InitKeyframe(scene, obj, f):
    #select object for keyframing
    object = obj
    bpy.context.scene.frame_set(f) 

#setting a keyframe
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
