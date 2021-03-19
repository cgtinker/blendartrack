import bpy
from bpy_extras.object_utils import world_to_camera_view
import mathutils


'''
screen_space_point:
Where (0, 0) is the bottom left and (1, 1) is the top right of the camera frame. 
values outside 0-1 are also supported. 
A negative ‘z’ value means the point is behind the camera.
'''


def world_to_camera_screen_space(scene, camera, px, py, pz, aim_x, aim_y):
    # world point vector
    vec = mathutils.Vector((px, py, pz))
    # world point relative to camera screen space
    screen_space_point = world_to_camera_view(scene, camera, vec)

    # ref for aspect ratio of the scene resolution
    res_x = bpy.context.scene.render.resolution_x
    res_y = bpy.context.scene.render.resolution_y
    '''
    # if the object is out of bounds return the old shift
    if aim_x > 0.975 or aim_y > 0.975 or aim_x < 0.075 or aim_y < 0.075:
        shift_x = float(camera.data.shift_x)
        shift_y = float(camera.data.shift_y)
        return shift_x, shift_y
    '''
    # if the point isn't behind the camera
    if screen_space_point[2] > 0:
        screen_space_x = screen_space_point[0]
        screen_space_y = screen_space_point[1]

        # current camera shift
        cam_x = float(camera.data.shift_x)
        cam_y = float(camera.data.shift_y)

        # ratio depending on scene resolution
        ratio_x = res_x / res_y
        ratio_y = res_y / res_x

        # difference between target and screen space point
        offset_x, rx = get_relative_offset(aim_x, screen_space_x, -0.5)
        offset_y, ry = get_relative_offset(aim_y, screen_space_y, -0.5)

        # applying the scene resolution and removing the current shift to get the actual lens shift value
        if res_x < res_y:
            if rx == "screen_space":
                shift_x = -offset_x * ratio_x + cam_x
            if rx == "aim":
                shift_x = offset_x * ratio_x + cam_x

            if ry == "screen_space":
                shift_y = -offset_y + cam_y
            if ry == "aim":
                shift_y = offset_y + cam_y

        else:
            if rx == "screen_space":
                shift_x = -offset_x + cam_x
            if rx == "aim":
                shift_x = offset_x + cam_x

            if ry == "screen_space":
                shift_y = -offset_y * ratio_y + cam_y
            if ry == "aim":
                shift_y = offset_y * ratio_y + cam_y

        return shift_x, shift_y


def get_relative_offset(aim, screen_space, offset):
    # fixing the space shift but keeping values normalized
    # -a + 0.5, -b + 0.5 to shift the space in camera shift uv space
    if screen_space > aim:
        offset = (-screen_space + offset) - (-aim + offset)
        r = "screen_space"
    else:
        offset = (-aim + offset) - (-screen_space + offset)
        r = "aim"
    return offset, r
