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


def add_list_to_collection(objects, name):
    if collection_exists(name):
        for o in objects:
            link_obj_to_collection(o, name)
    else:
        create_collection(name, True)
        for o in objects:
            link_obj_to_collection(o, name)


def add_obj_to_collection(name, m_object):
    if collection_exists(name):
        link_obj_to_collection(m_object, name)

    else:
        create_collection(name, True)
        link_obj_to_collection(m_object, name)


def link_obj_to_collection(m_object, name):
    if m_object.name in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.unlink(m_object)
        collection = bpy.data.collections.get(name)
        collection.objects.link(m_object)
