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


def set_camera_focal_length(focal_length, camera):
    # focal length accepts up to 6 digits before changing values randomly
    if round(camera.data.lens, 6) != round(focal_length, 6):
        camera.data.lens = round(focal_length, 6)
        camera.data.keyframe_insert('lens')


def set_camera_lens_shift(shift_x, shift_y, camera):
    # camera lens shift accepts up to 9 digits before changing values randomly
    if round(camera.data.shift_x, 9) != round(shift_x, 9):
        camera.data.shift_x = round(shift_x, 10)
        camera.data.keyframe_insert('shift_x')

    if round(camera.data.shift_y, 9) != round(shift_y, 9):
        camera.data.shift_y = round(shift_y, 9)
        camera.data.keyframe_insert('shift_y')


def set_camera_sensor(sensor_width, sensor_height, sensor_fit, camera):
    camera.data.sensor_fit = sensor_fit
    camera.data.sensor_width = sensor_width
    camera.data.sensor_height = sensor_height
