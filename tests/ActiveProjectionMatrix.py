"""
prints the active projection matrix
included for debugging and testing
"""


def print_projection_matrix(context, camera, render):
    # compute projection matrix -> Returns: 4x4 projection matrix
    projection_mat = camera.calc_matrix_camera(
        context.evaluated_depsgraph_get(),
        x=render.resolution_x,
        y=render.resolution_y,
        scale_x=render.pixel_aspect_x,
        scale_y=render.pixel_aspect_y
    )
    print(projection_mat)
