import bpy
import rigify
from utils.blend import data, objects, scene


# Todo: generate at other rig pos!!!
def generate(base_rig_name):
    objects.deselect_all()
    data.purge_orphan_data()

    context = scene.get_context()
    metarig = bpy.data.objects[base_rig_name]

    if metarig is not None:
        metarig.select_set(True)
        rigify.generate.generate_rig(context, metarig)
