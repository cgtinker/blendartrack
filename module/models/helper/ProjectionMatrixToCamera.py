# getting aspect and layout for projection calculations
def get_screen_aspect_ratio(resolution_x, resolution_y):
    print("wtf i have it??")
    if resolution_y > resolution_x:
        aspect = (resolution_y / resolution_x) * 2
        fit = 'X'
    else:
        aspect = (resolution_x / resolution_y) * 2
        fit = 'Y'

    return aspect, fit


def get_camera_focal_length(x, y, aspect, fit, sensor_width):
    # if res_y > res x, the matrix x value is used to determine the focal length
    if fit == "X":
        focal_length_in_mm = x / (aspect / sensor_width)
    else:
        focal_length_in_mm = y / (aspect / sensor_width)

    return focal_length_in_mm


# lens shift depends on scene resolution aspect ratio
def get_lens_shift(a, b, aspect, fit):
    if fit == 'X':
        shift_x = a / aspect
        shift_y = b / 2

    else:
        shift_x = a / 2
        shift_y = b / aspect

    return shift_x, shift_y
