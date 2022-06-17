import src.utils.blend.objects
import src.utils.blend.scene
from ....utils.blend import objects, data, scene, armature, viewport
# todo: import error just ignored..?
import rigify
import bpy


#todo: should be in blend.utils
def enable_addon(title):
    bpy.ops.preferences.addon_enable(module=title)
    print("enabled addon:", title)


def add(name="face_armature"):
    # clean up
    src.utils.blend.scene.purge_orphan_data()
    objects.deselect_all()
    enable_addon("rigify")

    context = scene.get_context()

    # todo -> blend
    arm = armature.add_armature(name)
    arm_obj = bpy.data.objects.new(name, arm)
    src.utils.blend.objects.objects.link(arm_obj)

    # select armature
    arm_obj.select_set(True)
    src.utils.blend.objects.objects.active = arm_obj
    
    # toggle edit mode
    src.utils.blend.scene.set_edit_mode()

    # adds super face by rigify
    add_rigify_face(context)
    return arm_obj

    
def add_rigify_face(context, metarig_type="faces.super_face"):
    if context.mode == 'EDIT_ARMATURE':
        try:
            rig = rigify.rig_lists.rigs[metarig_type]["module"]
            create_sample = rig.create_sample
        except (ImportError, AttributeError, KeyError):
            raise Exception("rig type '" + metarig_type + "' has no sample.")
        else:
            create_sample(context.active_object)
        finally:
            src.utils.blend.scene.set_object_mode()

        return {'FINISHED'}
