import bpy
import rigify

rig_is_generated = True


def DeselectAll():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)


DeselectAll()

if rig_is_generated:
    # remove all orphan data blocks
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)

    # get back to scene context
    context = bpy.context
    scene = context.scene
    metarig = bpy.data.objects['face_armature']  # object name
    metarig.select_set(True)
    rigify.generate.generate_rig(context, metarig)

DeselectAll()