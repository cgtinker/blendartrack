import bpy


def hide_collection_viewport(name, status):
    if collection_exists(name):
        collection = bpy.data.collections.get(name)
        collection.hide_viewport = status


def collection_exists(name):
    for collection in bpy.data.collections:
        if collection.name == name:
            return True
    return False


def create_collection(name, link):
    if collection_exists(name):
        return False
    else:
        collection = bpy.data.collections.new(name)
        if link:
            bpy.context.scene.collection.children.link(collection)
        return True


def remove_collection(name, remove_objects):
    if collection_exists(name):
        collection = bpy.data.collections.get(name)
        if collection:
            if remove_objects:
                obs = [o for o in collection.objects if o.users == 1]
                while obs:
                    bpy.data.objects.remove(obs.pop())
        bpy.data.collections.remove(collection)


def add_to_collection(name, objects):
    if collection_exists(name):
        collection = bpy.data.collections.get(name)
        collection.objects.link(objects)
