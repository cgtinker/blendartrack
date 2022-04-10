from mathutils import Vector
from .....utils.math import vector_math


def get_height_scale_difference(empties, bones):
    # empty locations for reference
    # TODO: copypasta
    empt_bot = empties["chin"].location
    empt_top = vector_math.get_center_point(
        empties["forehead.L"].location,
        empties["forehead.R"].location
        )

    # bone locations for reference
    bone_bot = bones["chin"].location
    bone_top = vector_math.get_center_point(
        bones["forehead.L"].location,
        bones["forehead.R"].location
        )

    # get distances
    empt_dist = vector_math.get_vector_distance(empt_bot, empt_top)
    bone_dist = vector_math.get_vector_distance(bone_bot, bone_top)

    dist = (empt_dist - bone_dist) / empt_dist
    return dist


def get_width_scale_difference(empties, bones):
    empt_right = empties["jaw.R"].location
    empt_left = empties["jaw.L"].location

    bone_right = bones["jaw.R"].location
    bone_left = bones["jaw.L"].location

    empt_dist = vector_math.get_vector_distance(empt_right, empt_left)
    bone_dist = vector_math.get_vector_distance(bone_right, bone_left)

    dist = (empt_dist - bone_dist) / empt_dist
    return dist


def get_rotation_difference(empties, bones):
    empt_bot = empties["chin"].location
    empt_top = vector_math.get_center_point(
        empties["forehead.L"].location,
        empties["forehead.R"].location
        )

    # bone locations for reference
    bone_bot = bones["chin"].location
    bone_top = vector_math.get_center_point(
        bones["forehead.L"].location,
        bones["forehead.R"].location
        )

    # zero_vec = vector_math.get_vector_from_points(Vector((0, 0, 0)), Vector((0, 0, 1)))
    empt_ref = vector_math.get_vector_from_points(empt_bot, empt_top)
    bone_ref = vector_math.get_vector_from_points(bone_bot, bone_top)

    angle = vector_math.get_angle_between_vectors(empt_ref, bone_ref)
    return angle