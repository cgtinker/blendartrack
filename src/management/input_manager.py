"""
# for manual debugging
import bpy
import sys
import os
# getting access to the current dir - necessary to access blender file location
blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
    sys.path.append(blend_dir)
"""

import bpy
import mathutils

from . import execution_handler
from ..setup import compositing
from ..setup.rig.diver_rig import rigify_generate_rig, add_bone_constraints
from ..setup.rig.face_rig import align_face_rig, align_bones, add_face_rig
from ..setup.rig.transfer_rig import animation_transfer
from ..utils import pathing, reference_names
from ..utils.blend import armature, objects
from ..utils.blend import reference


# todo: implement better event struct
def file_to_load(m_path):
    print("\n" + "processing input path:", m_path)
    paths, valid = pathing.process_path(m_path)
    if valid:
        manager = execution_handler.ExecutionManager()
        manager.import_models(paths)
    print("\n" + "file imported")


def internal_compositing():
    tree = compositing.CompositingTree()
    compositing.set_internal_compositing(tree)
    compositing.setup_render()
    print("set internal compositing")


def external_compositing():
    tree = compositing.CompositingTree()
    compositing.set_external_compositing(tree)
    compositing.setup_render()
    print("set external compositing")


def generate_face_rig():
    print("generating face rig")
    rig = add_face_rig.add("base_face_rig")
    aligned_rig = align_face_rig.FaceAligner(rig.name)
    align_bones.align(aligned_rig.armature)
    try:
        parent = objects.get_object(reference_names.head_controller)
        # align rig
        aligned_rig.armature.scale = parent.scale
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        # reset parent?
        parent.location = mathutils.Vector((0, 0, 0))
        parent.rotation_euler = mathutils.Euler((0, 0, 0))

    except KeyError:
        print("Cannot copy scale to rig")


def generate_driver_rig():
    arm = get_armature_by_selection_or_name("base_face_rig")
    rigify_generate_rig.generate(arm)
    rig = bpy.context.selected_objects[0]
    # rig = armature.get_armature("rig")
    rig.name = "driver_rig"
    rig.data.name = "driver_rig"
    add_bone_constraints.add(rig)

    bpy.data.armatures["driver_rig"].layers[29] = True


def update_driver_influence():
    arm = get_armature_by_selection_or_name("driver_rig")
    print(arm.name, arm)
    add_bone_constraints.update(arm)


def get_armature_by_selection_or_name(name):
    selected_obj = reference.get_selected_object()
    try:
        if selected_obj.type == 'ARMATURE':
            return selected_obj
        else:
            return armature.get_armature(name)
    except AttributeError:
        return armature.get_armature(name)


def transfer_rig():
    arm = get_armature_by_selection_or_name("driver_rig")
    animation_transfer.save_as_action(arm)


"""
# for manual debugging
manual_dir = "/Users/Scylla/Downloads/2021-01-06_17-12-08_face"
manual_file = "/Users/Scylla/Downloads/2021-03-12_00-29-55_cam.zip"
file_to_load(manual_file)
"""
