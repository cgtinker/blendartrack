from ....utils.blend import viewport, scene
from ..diver_rig import add_bone_constraints
import bpy
import importlib

importlib.reload(scene)


# TODO: apply action directly to target rig.
def save_as_action(arm):
    # referencing
    # get driver bones
    viewport.set_pose_mode()
    driver_bones = []
    bone_dict = add_bone_constraints.get_constraint_dict()

    print("get diver bones")
    for bone in arm.pose.bones:
        try:
            constrained_bone = bone_dict[bone.name][0]
            driver_bones.append(bone)
        except KeyError:
            pass

    # select driver bones
    bpy.ops.pose.select_all(action='DESELECT') # todo: util.blend
    for b in driver_bones:
        b.bone.select = True
    """
    # create new action
    animation_data = arm.animation_data
    animation_data.use_nla = False
    """
    # baking
    print("backing animation data to keyframes")
    bpy.ops.nla.bake(
        frame_start=scene.get_frame_start(),
        frame_end=scene.get_frame_end(),
        only_selected=True,
        visual_keying=True,
        use_current_action=True,
        bake_types={'POSE'}
    )

    viewport.set_object_mode()
    print("finished backing")
    # todo: select action on target rig
    # transfer active action
    # action = driver_rig.animation_data.action
    # target_rig.animation_data.action = animation_data.action
