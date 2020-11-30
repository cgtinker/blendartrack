# import bpy

"""
# https://answers.unity.com/questions/1359718/what-do-the-values-in-the-matrix4x4-for-cameraproj.html
# http://www.songho.ca/opengl/gl_projectionmatrix.html
Unity Projection Matrix -> OpenGL (same as blender):
r = right, l = left, n = near, f = far, t = top, b = bot

(x  0  a  0)    x = 2 * n / (r - l)         y = 2 * n / (t - b)
(0  y  b  0)    a = (r + l) / (r - l)       b = (t + b) / (t - b)
(0  0  c  d)    c = -(f + n) / (f - n)      d = -(2 * f * n) / (f - n)
(0  0  e  0)    e = -1

(   scale   ,   0       ,  offset           ,     0         )
(   0       ,   scale   ,  offset           ,     0         )
(   0       ,   0       ,  depth (scales Z) , depth (const) )
(   0       ,   0       ,  perspective      ,     0         )

a, b -> affected by res x, res y
c, d -> affected by clip start, clip end - can be ignored for retargeting
x, y -> affected by focal length & sensor size (goes hand in hand)
e -> open gl coord system (usually 1, flipped x for unity / blender)
"""


# focal length depends on scene resolution aspect ratio
def get_screen_aspect_ratio(resolution_x, resolution_y):
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


'''
def get_scene_resolution(scene):
    scale = scene.render.resolution_percentage / 100
    pixel_aspect_ratio = scene.render.pixel_aspect_x / scene.render.pixel_aspect_y
    return scale, pixel_aspect_ratio
'''

"""
def get_sensor_size_in_mm(
        sensor_fit, rec_width, rec_height,
        screen_width, screen_height, scale,
        pixel_aspect_ratio):

    if sensor_fit == 'VERTICAL':
        # if the sensor height is fixed (sensor fit is vertical),

        sensor_width = (screen_width * scale / pixel_aspect_ratio) / rec_height
        sensor_height = (screen_height * scale) / rec_width

        #sensor_width = (screen_width * scale) / rec_width / pixel_aspect_ratio
        #sensor_height = (screen_height * scale) / rec_height

        print("sensor w: ", sensor_width, "sensor_h", sensor_height)
        return sensor_width, sensor_height

    else:  # 'HORIZONTAL' and 'AUTO'
        # if the sensor width is fixed (sensor fit is horizontal),
        sensor_width = (screen_width * scale) / rec_width
        sensor_height = (screen_height * scale) * pixel_aspect_ratio / rec_height
        print("sensor w: ", sensor_width, "sensor_h", sensor_height)
        return sensor_width, sensor_height


# FX = fx * (W/w), FY = fy * (H/h) - physical focal length
# FX / FY = f_in_mm, W/H = sensor_in_mm, w/h = rec_px, fx, fy = f in mm
def get_focal_length(
        fl_x, fl_y, rec_width, rec_height, sensor_width,
        sensor_height):
    f_in_mm_x = fl_x * sensor_width / rec_width
    f_in_mm_y = fl_y * sensor_height / rec_height

    print('fx', f_in_mm_x, 'flx', fl_x, 'sensorW', sensor_width, 'recW', rec_width)
    print('fy', f_in_mm_y, 'fly', fl_y, 'sensorH', sensor_height, 'recH', rec_height)

    return f_in_mm_x


# X0 = x0 * (W / w) - physical lens shift
def get_lens_shift(
        pp_x, pp_y, rec_width, rec_height, scale):
    shift_x = (rec_width / 2) / pp_x - scale
    shift_y = (rec_height / 2) / pp_y - scale

    print('shiftX', shift_x, 'recW', rec_width, 'ppX', pp_x, scale)
    print('shiftY', shift_y, 'recH', rec_height, 'ppY', pp_y, scale)
    
    return shift_x, shift_y
"""
