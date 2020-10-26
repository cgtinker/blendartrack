pi = 3.14159265


# getting translation
def split_pos_data(data):
    px = float(data['pos']['x'])
    py = float(data['pos']['y'])
    pz = float(data['pos']['z'])
    return px, py, pz


# getting rotation
def split_rot_data(data):
    rx = float(data['rot']['x'])
    ry = float(data['rot']['y'])
    rz = float(data['rot']['z'])
    return rx, ry, rz
