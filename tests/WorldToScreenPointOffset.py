import bpy
from bpy_extras.object_utils import world_to_camera_view
import mathutils

'''
this script helps to manually check the position of a point in global space
in it's relative screen space. the point gets compared to the target screen space destination.

the scene camera gets shifted to fix the offset.

screen_space_point:
Where (0, 0) is the bottom left and (1, 1) is the top right of the camera frame. 
values outside 0-1 are also supported. 
A negative ‘z’ value means the point is behind the camera.

screen space point to camera shift uv comparison
space        <==>  shift
( 0.0,  0.0)  ==  ( 0.5,  0.5)
( 0.5,  0.5)  ==  ( 0.0,  0.0)
(-0.5, -0.5)  ==  ( 1.0,  1.0)
'''


def world_to_camera_screen_space(scene, camera, vec, target_x, target_y, res_x, res_y):
    screen_space_point = world_to_camera_view(scene, camera, vec)
    print("")
    print("")
    print("VECTOR to reach")
    print("input: ", "x", screen_space_point[0], "y", screen_space_point[1])
    print("target:", "x", target_x, "y", target_y)
    print("")
    if target_x > 0.975 or target_y > 0.975 or target_x < 0.075 or target_y < 0.075:
        return

    # if the point isn't behind the camera
    if screen_space_point[2] > 0:
        # current screen space representation
        screen_space_x = screen_space_point[0]
        screen_space_y = screen_space_point[1]

        # current camera shift
        cam_x = float(camera.data.shift_x)
        cam_y = float(camera.data.shift_y)

        # ratio depending on scene resolution
        ratio_x = res_x / res_y
        ratio_y = res_y / res_x

        # transformed difference between target and screen space point
        offset_x, rx = get_relative_offset(target_x, screen_space_x, -0.5)
        offset_y, ry = get_relative_offset(target_y, screen_space_y, -0.5)
        print("offset", offset_x, "rx", rx, "|| offset", offset_y, "ry", ry)

        # print("offset_x",offset_x,"offset_y", offset_y)

        if res_x < res_y:
            if rx == "X":
                shift_x = -offset_x * ratio_x + cam_x
            if rx == "Y":
                shift_x = offset_x * ratio_x + cam_x

            if ry == "X":
                shift_y = -offset_y + cam_y
            if ry == "Y":
                shift_y = offset_y + cam_y

            print("shift x", shift_x, "shift y", shift_y, "|| rx", rx, "|| ry", ry)
            camera.data.shift_x = shift_x
            camera.data.shift_y = shift_y
            print("")
            screen_space_point = world_to_camera_view(scene, camera, vec)
            print("vector:", screen_space_point, "x", target_x, "y", target_y)

            # aligning screen point space point to lens shift uv space

        else:
            if rx == "X":
                shift_x = -offset_x + cam_x
            if rx == "Y":
                shift_x = offset_x + cam_x

            if ry == "X":
                shift_y = -offset_y * ratio_y + cam_y
            if ry == "Y":
                shift_y = offset_y * ratio_y + cam_y

            print("shift x", shift_x, "shift y", shift_y, "|| rx", rx, "|| ry", ry)
            camera.data.shift_x = shift_x
            camera.data.shift_y = shift_y
            print("")
            screen_space_point = world_to_camera_view(scene, camera, vec)
            print("vector:", screen_space_point, "x", target_x, "y", target_y)


def get_relative_offset(a, b, offset):
    # fixing the space shift but keeping values normalized
    # -a + 0.5, -b + 0.5 to shift the space in camera shift uv space
    if b > a:
        offset = (-b + offset) - (-a + offset)
        r = "X"
    else:
        offset = (-a + offset) - (-b + offset)
        r = "Y"
    return offset, r;


#  test vector as target point
vec = mathutils.Vector((0, 0, 0.0))

scene = bpy.context.scene
camera = scene.camera

res_x = bpy.context.scene.render.resolution_x
res_y = bpy.context.scene.render.resolution_y

# where the object should be visible
target_x = .1
target_y = .2

world_to_camera_screen_space(scene, camera, vec, target_x, target_y, res_x, res_y)
