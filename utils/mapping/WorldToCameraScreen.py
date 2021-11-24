import bpy
from bpy_extras.object_utils import world_to_camera_view
from utils.validation import ValidateValue
from importlib import reload
import mathutils

reload(ValidateValue)


'''
screen_space_point:
Where (0, 0) is the bottom left and (1, 1) is the top right of the camera frame. 
values outside 0-1 are also supported. 
A negative ‘z’ value means the point is behind the camera.
'''


def world_to_camera_screen_space(scene, camera, px, py, pz, aim_x, aim_y):
    # return if input isn't valid
    a, b, valid = is_input_valid(aim_x, aim_y, camera, px, py, pz)
    if not valid:
        return a, b

    # get scene res info and obj screen space position
    screen_space_point = get_obj_world_to_camera_view_position(camera, px, py, pz, scene)
    res_x, res_y = get_screen_resolution()
    target_in_front_of_camera = is_in_front_camera(screen_space_point)

    # trying to match ar app and blender render position
    if target_in_front_of_camera:
        screen_space_x, screen_space_y = get_screen_space_uv_pos(screen_space_point)
        cam_x, cam_y = get_current_lens_shift(camera)
        ratio_x, ratio_y = get_screen_resolution_ratio(res_x, res_y)

        # offset between object render position of blender and app
        offset_x, offset_y, rx, ry = get_ar_to_bpy_render_offset(
            aim_x, aim_y, screen_space_x, screen_space_y)

        # lens shift to mitigate the difference
        shift_x, shift_y = get_accurate_lens_shift(
            cam_x, cam_y, offset_x, offset_y,
            ratio_x, ratio_y, res_x, res_y, rx, ry)

        return shift_x, shift_y

    # if target behind camera return current lens shift
    else:
        return get_current_lens_shift(camera)


def get_accurate_lens_shift(
        cam_x, cam_y, offset_x, offset_y,
        ratio_x, ratio_y, res_x, res_y, rx, ry):
    # landscape mode
    if res_x < res_y:
        shift_x, shift_y = get_lens_shift_in_landscape_mode(
            cam_x, cam_y, offset_x, offset_y, ratio_x, rx, ry)
    # portrait mode
    else:
        shift_x, shift_y = get_lens_shift_in_portrait_mode(
            cam_x, cam_y, offset_x, offset_y, ratio_y, rx, ry)
    return shift_x, shift_y


def get_relative_offset(aim, screen_space, offset):
    """
    fixing the space shift while keeping values normalized
    -a + 0.5, -b + 0.5 to shift the space in camera shift uv space
    """
    if screen_space > aim:
        offset = (-screen_space + offset) - (-aim + offset)
        r = "screen_space"
    else:
        offset = (-aim + offset) - (-screen_space + offset)
        r = "aim"
    return offset, r


def get_lens_shift_in_portrait_mode(cam_x, cam_y, offset_x, offset_y, ratio_y, rx, ry):
    shift_x, shift_y = 0, 0
    if rx == "screen_space":
        shift_x = -offset_x + cam_x
    if rx == "aim":
        shift_x = offset_x + cam_x
    if ry == "screen_space":
        shift_y = -offset_y * ratio_y + cam_y
    if ry == "aim":
        shift_y = offset_y * ratio_y + cam_y
    return shift_x, shift_y


def get_lens_shift_in_landscape_mode(cam_x, cam_y, offset_x, offset_y, ratio_x, rx, ry):
    shift_x, shift_y = 0, 0
    if rx == "screen_space":
        shift_x = -offset_x * ratio_x + cam_x
    if rx == "aim":
        shift_x = offset_x * ratio_x + cam_x
    if ry == "screen_space":
        shift_y = -offset_y + cam_y
    if ry == "aim":
        shift_y = offset_y + cam_y
    return shift_x, shift_y


def is_in_front_camera(screen_space_point):
    if screen_space_point[2] > 0:
        return True
    else:
        return False


def get_ar_to_bpy_render_offset(aim_x, aim_y, screen_space_x, screen_space_y):
    offset_x, rx = get_relative_offset(aim_x, screen_space_x, -0.5)
    offset_y, ry = get_relative_offset(aim_y, screen_space_y, -0.5)
    return offset_x, offset_y, rx, ry


def get_screen_space_uv_pos(screen_space_point):
    screen_space_x = screen_space_point[0]
    screen_space_y = screen_space_point[1]
    return screen_space_x, screen_space_y


def get_screen_resolution_ratio(res_x, res_y):
    ratio_x = res_x / res_y
    ratio_y = res_y / res_x
    return ratio_x, ratio_y


def get_current_lens_shift(camera):
    cam_x = float(camera.data.shift_x)
    cam_y = float(camera.data.shift_y)
    return cam_x, cam_y


def get_screen_resolution():
    res_x = bpy.context.scene.render.resolution_x
    res_y = bpy.context.scene.render.resolution_y
    return res_x, res_y


def get_obj_world_to_camera_view_position(camera, px, py, pz, scene):
    vec = mathutils.Vector((px, py, pz))
    screen_space_point = world_to_camera_view(scene, camera, vec)
    return screen_space_point


def is_input_valid(aim_x, aim_y, camera, px, py, pz):
    float_list = [px, py, pz, aim_x, aim_y]
    for f in float_list:
        if ValidateValue.is_float(f):
            return "", "", True
        else:
            cam_x, cam_y = get_current_lens_shift(camera)
            return cam_x, cam_y, False
