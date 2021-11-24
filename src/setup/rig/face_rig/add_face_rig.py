from src.utils.blend import objects, data, scene, armature, viewport
# todo: import error just ignored..?
import rigify
import bpy
import importlib

importlib.reload(armature)


#todo: should be in blend.utils
def enable_addon(title):
    bpy.ops.preferences.addon_enable(module=title)
    print("enabled addon:", title)


# Todo: return armature
def add(name="face_armature"):
    # clean up
    data.purge_orphan_data()
    objects.deselect_all()
    enable_addon("rigify")

    context = scene.get_context()

    # todo -> blend
    arm = armature.add_armature(name)
    arm_obj = bpy.data.objects.new(name, arm)
    context.scene.collection.objects.link(arm_obj)

    # select armature
    arm_obj.select_set(True)
    context.view_layer.objects.active = arm_obj
    
    # toggle edit mode
    viewport.set_edit_mode()

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
            viewport.set_object_mode()

        return {'FINISHED'}
