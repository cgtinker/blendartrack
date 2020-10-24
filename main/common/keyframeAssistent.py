pi = 3.14159265


# preparing to keyframe
def init_keyframe(frame, scene, obj):
    # select object for key framing
    # TODO: Test import fuctionality after refactoring
    object = obj
    scene.frame_set(frame)


# setting translation
def pos_keyframes(px, py, pz, obj):
    # set camera translation
    obj.location.x = px
    obj.location.y = py
    obj.location.z = pz
    # set translation keyframe
    obj.keyframe_insert(data_path="location")


# setting rotation
def rot_keyframes(rx, ry, rz, obj):
    obj.rotation_mode = 'XYZ'
    obj.rotation_euler[0] = rx * (pi / 180.0)
    obj.rotation_euler[1] = ry * (pi / 180.0)
    obj.rotation_euler[2] = rz * (pi / 180.0)
    # set rotation keyframe
    obj.keyframe_insert("rotation_euler")
