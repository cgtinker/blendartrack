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

    if isinstance(m_vector, Vector):
        obj.rotation_euler = m_vector
        obj.keyframe_insert("rotation_euler")
    else:
        print("vector rotation not valid for:", obj.name)


# setting shape key
def set_shape_key(index, value, obj, frame):
    if isinstance(value, float):
        obj.shape_keys.key_blocks[index].value = value
        obj.shape_keys.key_blocks[index].keyframe_insert("value", frame=frame)
    else:
        print("shape key cannot be applied to", obj.name, "at frame", frame)


def set_camera_focal_length(focal_length, camera):
    if isinstance(focal_length, float):
        # focal length accepts up to 6 digits before changing values randomly
        if round(camera.data.lens, 6) != round(focal_length, 6):
            camera.data.lens = round(focal_length, 6)
            camera.data.keyframe_insert('lens')
    else:
        print("focal length not valid for:", camera.name)


def set_camera_lens_shift(shift_x, shift_y, camera):
    if isinstance(shift_x, float):
        # camera lens shift accepts up to 9 digits before changing values randomly
        if round(camera.data.shift_x, 9) != round(shift_x, 9):
            camera.data.shift_x = round(shift_x, 10)
            camera.data.keyframe_insert('shift_x')
    else:
        print("lens shift_x cannot be applied")

    if isinstance(shift_y, float):
        if round(camera.data.shift_y, 9) != round(shift_y, 9):
            camera.data.shift_y = round(shift_y, 9)
            camera.data.keyframe_insert('shift_y')
    else:
        print("lens shit_y cannot be applied")


def set_camera_sensor(sensor_width, sensor_height, sensor_fit, camera):
    if isinstance(sensor_fit, float):
        camera.data.sensor_fit = sensor_fit
    else:
        print("sensor fit cannot be applied")

    if isinstance(sensor_width, float):
        camera.data.sensor_width = sensor_width
    else:
        print("sensor height cannot be applied")

    if isinstance(sensor_height, float):
        camera.data.sensor_height = sensor_height
    else:
        print("sensor height cannot be applied")


def keyframe_geometry(f_curves, frame, positions):
    for fcu, position in zip(f_curves, positions):
        fcu.keyframe_points.insert(
            frame, position, options={'FAST'}, keyframe_type='JITTER')
