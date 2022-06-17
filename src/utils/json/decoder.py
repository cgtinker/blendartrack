def get_pos_data(data):
    px = float(data['pos']['x'])
    py = float(data['pos']['y'])
    pz = float(data['pos']['z'])
    return px, py, pz


def get_vert_data(data):
    px = float(data['x'])
    py = float(data['y'])
    pz = float(data['z'])
    return px, py, pz


def get_two_dim_data(data):
    px = float(data['x'])
    py = float(data['y'])
    return px, py


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
    frame = int(data['frame'])
    fl_x = float(data['flX'])
    fl_y = float(data['flY'])
    pp_x = float(data['ppX'])
    pp_y = float(data['ppY'])
    return fl_x, fl_y, pp_x, pp_y, frame


def get_device_resolution(data):
    screen_width =  float(data['screenWidth'])
    screen_height = float(data['screenHeight'])
    return screen_width, screen_height


def get_camera_config(data):
    fps = int(data['fps'])
    rec_width = int(data['width'])
    rec_height = int(data['height'])
    return fps, rec_width, rec_height


# (x  0  a  0)   (e00, e01, e02, e03)
# (0  y  b  0)   (e10, e11, e12, e13)
# (0  0  c  d)   (e20, e21, e22, e23)
# (0  0  e  0)   (e30, e31, e32, e33)
def get_camera_projection_values(data):
    frame = int(data['frame'])
    x = float(data['cameraProjectionMatrix']['e00'])
    y = float(data['cameraProjectionMatrix']['e11'])
    a = float(data['cameraProjectionMatrix']['e02'])
    b = float(data['cameraProjectionMatrix']['e12'])
    c = float(data['cameraProjectionMatrix']['e22'])
    d = float(data['cameraProjectionMatrix']['e23'])
    return x, y, a, b, c, d, frame
