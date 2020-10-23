pi = 3.14159265

#preparing to keyframe
def InitKeyframe(frame, scene, obj):
    #select object for keyframing
    object = obj
    bpy.context.scene.frame_set(frame)

#setting translation
def PosKeyframes(px, py, pz, obj):
    #set camera translation
    obj.location.x = px;
    obj.location.y = py;
    obj.location.z = pz;
    #set translation keyframe
    obj.keyframe_insert(data_path="location")

#setting rotation
def RotKeyframes(rx, ry, rz, obj):
    obj.rotation_mode = 'XYZ'
    obj.rotation_euler[0] = rx*(pi/180.0)
    obj.rotation_euler[1] = ry*(pi/180.0)
    obj.rotation_euler[2] = rz*(pi/180.0)
    #set rotation keyframe
    obj.keyframe_insert("rotation_euler")
