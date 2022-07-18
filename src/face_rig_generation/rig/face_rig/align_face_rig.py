import bpy
import mathutils
from mathutils import Vector

from .align_rig import get_difference, apply_transforms
from ....utils.blend import armature, scene


class ReferenceLocation(object):
    def __init__(self, name: str, obj, _type: str, arm):
        self.name = name    
        self.object = obj
        self.type = _type
        self.armature = arm
        self.local_location = self.get_local_location()
        self.location = self.get_location()
        
    def get_location(self):
        if self.type == "empty":
            self.location = self.object.location
            # self.location = self.object.matrix_world.translation
        elif self.type == "bone":
            self.location = armature.get_global_bone_head_position(self.armature, self.object)
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
    def __init__(self, armature_name: str = None):
        # bone -- android -- ios
        self.location_references = [
            ["chin",        "FaceEmpty_152",    "FaceEmpty_1047"],
            ["forehead.L",  "FaceEmpty_338",    "FaceEmpty_853"],
            ["forehead.R",  "FaceEmpty_109",    "FaceEmpty_425"],
            ["jaw.L",       "FaceEmpty_435",    "FaceEmpty_1008"],
            ["jaw.R",       "FaceEmpty_215",    "FaceEmpty_939"]
        ]

        self.is_android = False
        if scene.get_user().enum_device_type == "Android":
            self.is_android = True
        print("Attempt to align", scene.get_user().enum_device_type, "face rig")
        self.armature = armature.get_armature(armature_name)
        self.bones = armature.get_armature_bones(self.armature)
        self.adjustment_bones = self.get_rig_adjustment_bones()
        self.adjustment_empties = self.get_face_adjustment_empties()

        self.set_origin()
        # depreciated in 2.2:
        # self.set_rotation()
        # self.set_scale()
        self.set_location()

        print("apply transforms")
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
        if angle != 0:
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
        for bone_name, android_empty, ios_empty in self.location_references:
            obj = ReferenceLocation(bone_name, self.bones[bone_name], "bone", self.armature)
            face_bones[bone_name] = obj
        return face_bones

    def get_face_adjustment_empties(self):
        empties = {}
        for bone_name, android_empty, ios_empty in self.location_references:
            # todo: bpy to blend
            if self.is_android:
                obj = ReferenceLocation(android_empty, bpy.data.objects.get(android_empty), "empty", self.armature)
            else:
                obj = ReferenceLocation(ios_empty, bpy.data.objects.get(ios_empty), "empty", self.armature)
            empties[bone_name] = obj
        return empties

    def get_bones(self):
        return self.bones

    def get_armature(self):
        return self.armature
