import bpy


def add_copy_location_constraint(obj, target_obj, use_offset):
    constraint = obj.constraints.new('COPY_LOCATION')
    constraint.target = target_obj
    constraint.use_offset = use_offset


def add_copy_rotation_constraint(obj, target_obj, invert_y):
    constraint = obj.constraints.new('COPY_ROTATION')
    constraint.target = target_obj
    if invert_y:
        constraint.invert_y = True
