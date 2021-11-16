import bpy
import mathutils
from mathutils import Vector

from setup.rig.face_rig.align_rig import get_difference, apply_transforms
from utils.blend import armature
from utils.math import data_format


class ReferenceLocation(object):
    def __init__(self, name, obj, _type):
        self.name = name    
        self.object = obj
        self.type = _type
        self.local_location = self.get_local_location()
        self.location = self.get_location()
        
    def get_location(self):
        if self.type == "droid_empty":
            self.location = self.object.location
        elif self.type == "bone":
            self.location = armature.get_global_bone_head_position(armature, self.object)
        else:
            self.location = None
            print("type not implemented")
        return self.location
    
    def get_local_location(self):
        if self.type == "bone":
            self.location = self.object.head_local
        else:
            self.location = self.object.location
        return self.location

    def is_bone_reference(self, name):
        if self.name == name:
            return True
        else:
            return False


class FaceAligner(object):
    def __init__(self, rig):
        self.android_location_references = [
            ["chin", "FaceEmpty_152"],
            ["forehead.L", "FaceEmpty_338"],
            ["forehead.R", "FaceEmpty_109"],
            ["jaw.L", "FaceEmpty_435"],
            ["jaw.R", "FaceEmpty_215"]
        ]

        self.armature = rig
        self.bones = armature.get_armature_bones(self.armature)
        self.adjustment_bones = self.get_rig_adjustment_bones()
        self.adjustment_empties = self.get_android_face_adjustment_empties()

        self.set_origin()
        self.set_rotation()
        self.set_scale()
        self.set_location()

        apply_transforms.apply_transforms_to_object(self.armature)

    def set_origin(self):
        new_origin = self.adjustment_bones["chin"].location
        # reset origin
        if new_origin != self.armature.location:
            bpy.ops.object.mode_set(mode='EDIT')
            self.armature.data.transform(mathutils.Matrix.Translation(-new_origin))
            self.armature.matrix_world.translation += new_origin
            bpy.ops.object.mode_set(mode='OBJECT')

    def set_rotation(self):
        angle = get_difference.get_rotation_difference(self.adjustment_empties, self.adjustment_bones)
        # rotation euler takes an angle and creates the according radians
        if data_format.angle_to_degrees(angle) != 0:
            self.armature.rotation_euler = Vector((self.armature.rotation_euler[0] + angle, 0, 0))

    def set_scale(self):
        # get scale difference and apply it before translating
        height_scale = get_difference.get_height_scale_difference(self.adjustment_empties, self.adjustment_bones)
        width_scale = get_difference.get_width_scale_difference(self.adjustment_empties, self.adjustment_bones)

        self.armature.scale = (
            self.armature.scale[0] + width_scale,
            self.armature.scale[1],
            self.armature.scale[2] + height_scale
        )

    def set_location(self):
        arm = self.armature.location
        bone = self.adjustment_bones["chin"].location
        empt = self.adjustment_empties["chin"].location

        destination = Vector((
            arm[0] + (empt[0] - bone[0]),
            arm[1] + (empt[1] - bone[1]),
            arm[2] + (empt[2] - bone[2]),
        ))

        self.armature.location = destination

    def get_rig_adjustment_bones(self):
        face_bones = {}
        for bone_name, empty in self.android_location_references:
            obj = ReferenceLocation(bone_name, self.bones[bone_name], "bone")
            face_bones[bone_name] = obj
        return face_bones

    def get_android_face_adjustment_empties(self):
        android_empties = {}
        for bone_name, empty in self.android_location_references:
            # todo: bpy to blend
            obj = ReferenceLocation(empty, bpy.data.objects.get(empty), "droid_empty")
            android_empties[bone_name] = obj
        return android_empties

    def get_bones(self):
        return self.bones

    def get_armature(self):
        return self.armature
