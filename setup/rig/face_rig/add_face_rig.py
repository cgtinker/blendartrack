from utils.blend import objects, data, scene, armature, collection, viewport
# todo: fix import error
import rigify


# Todo: return armature
def add(name="face_armature"):
    # clean up
    data.purge_orphan_data()
    objects.deselect_all()

    context = scene.get_context()
    m_scene = scene.get_scene()

    arm = armature.add_armature(name)
    collection.add_obj_to_collection(arm)

    # select armature
    arm.select_set(True)
    context.view_layer.objects.active = arm
    
    # toggle edit mode
    viewport.set_edit_mode()

    # adds super face by rigify
    rig = add_rigify_face(context)
    return rig

    
def add_rigify_face(context, metarig_type="faces.super_face"):
    create_sample = None
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

    return create_sample
