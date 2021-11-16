import bpy


def add_armature(name):
    arm = bpy.data.armatures.new(name)
    arm_obj = bpy.data.objects.new(name, arm)
    return arm


def get_armature(name="face_armature"):
    armature = bpy.data.objects[name]
    return armature


def get_armature_bones(armature):
    bones = armature.data.bones
    return bones


def get_global_bone_position(armature, bone):
    global_position = bone.head_local + armature.location
    return global_position


def get_global_bone_head_position(armature, bone):
    global_location = armature.matrix_world @ bone.head_local
    return global_location