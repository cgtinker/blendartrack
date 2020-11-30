# getting translation
def get_pos_data(data):
    px = float(data['pos']['x'])
    py = float(data['pos']['y'])
    pz = float(data['pos']['z'])
    return px, py, pz


# getting vertex data
def get_vert_data(data):
    px = float(data['x'])
    py = float(data['y'])
    pz = float(data['z'])
    return px, py, pz


def get_rot_data(data):
    rx = float(data['rot']['x'])
    ry = float(data['rot']['y'])
    rz = float(data['rot']['z'])
    return rx, ry, rz


def get_blend_shape(data):
    title = str(data['shapeKey'])
    value = float(data['value'])
    return title, value


def get_camera_intrinsics(data):
    frame = data['frame']
    fl_x = data['flX']
    fl_y = data['flY']
    pp_x = data['ppX']
    pp_y = data['ppY']
    return fl_x, fl_y, pp_x, pp_y, frame


def get_device_resolution(data):
    screen_width = data['screenWidth']
    screen_height = data['screenHeight']
    return screen_width, screen_height


def get_camera_config(data):
    fps = data['fps']
    rec_width = data['width']
    rec_height = data['height']
    return fps, rec_width, rec_height
