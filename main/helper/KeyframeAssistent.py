from mathutils import Vector
pi = 3.14159265


# preparing to keyframe
def init_keyframe(frame, scene):
    scene.frame_set(frame)


# get vector direction
def get_vector(px, py, pz):
    vector = Vector((px, py, pz))
    return vector


# setting translation
def set_pos_keyframe(px, py, pz, obj):
    m_vector = get_vector(px, py, pz)
    obj.location = m_vector
    obj.keyframe_insert(data_path="location")


# setting rotation
def set_rot_keyframe(rx, ry, rz, obj):
    obj.rotation_mode = 'XYZ'
    tmp = (pi/180.0)
    m_vector = get_vector(rx * tmp, ry * tmp, rz * tmp)
    obj.rotation_euler = m_vector
    obj.keyframe_insert("rotation_euler")


# setting shape key
def set_shape_key(index, value, obj, frame):
    obj.data.shape_keys.key_blocks[index].value = value
    obj.data.shape_keys.key_blocks[index].keyframe_insert("value", frame=frame)
