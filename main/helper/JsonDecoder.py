# getting translation
def split_pos_data(data):
    px = float(data['pos']['x'])
    py = float(data['pos']['y'])
    pz = float(data['pos']['z'])
    return px, py, pz


# getting vertex data
def split_vert_data(data):
    px = float(data['x'])
    py = float(data['y'])
    pz = float(data['z'])
    return px, py, pz


# getting rotation
def split_rot_data(data):
    rx = float(data['rot']['x'])
    ry = float(data['rot']['y'])
    rz = float(data['rot']['z'])
    return rx, ry, rz


def get_blend_shape(data):
    title = str(data['shapeKey'])
    value = float(data['value'])
    return title, value
