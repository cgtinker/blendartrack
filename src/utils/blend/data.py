import bpy


def purge_orphan_data():
    # remove all orphan data blocks
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)

    # remove all orphan armatures
    for armature in bpy.data.armatures:
        print(armature)
        if armature.users == 0:
            print("remove;", armature)
            bpy.data.armatures.remove(armature)
