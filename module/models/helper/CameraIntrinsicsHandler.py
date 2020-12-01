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


# getting aspect and layout for projection calculations
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
