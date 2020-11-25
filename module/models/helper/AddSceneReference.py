import bpy


# getting scene ref & adjusting scene frame end
# scene = bpy.context.scene


def get_selected_objects(amount):
    objects = len(bpy.context.selected_objects)

    if objects >= 1:
        objects = bpy.context.selected_objects

    else:
        objects = generate_empties(amount=amount, size=1)

    return objects


# new method for generating objects
def generate_empties(amount, size):
    empty_objects = []
    for cur in range(amount):
        obj = bpy.data.objects.new('Retarget_{}'.format(cur), None)
        # due to the new mechanism of "collection"
        bpy.context.scene.collection.objects.link(obj)

        obj.empty_display_size = size  # 2.8 empty_draw was replaced by empty_display
        obj.empty_display_type = 'ARROWS'

        # bpy.ops.object.empty_add(type='ARROWS', radius=size, align='WORLD', location=[0, 0, 0], rotation=[0, 0, 0])
        # obj = bpy.data.objects['Empty']
        # obj.name = 'Retarget_{}'.format(cur)
        empty_objects.append(obj)

    return empty_objects


# setting scene frame rate
def add_scene_properties(data):
    # getting scene ref & adjusting scene frame end
    m_scene = bpy.context.scene
    scene_frames = len(data)
    if m_scene.frame_end < scene_frames:
        m_scene.frame_end = scene_frames
    return m_scene


def get_obj_blend_shape_ref(obj):
    keys = obj.data.shape_keys.key_blocks
    return keys
