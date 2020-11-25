import bpy

# getting scene ref & adjusting scene frame end
scene = bpy.context.scene


def get_selected_objects(amount):
    objects = len(bpy.context.selected_objects)

    if objects >= 1:
        objects = bpy.context.selected_objects

    else:
        objects = generate_empties(amount=amount, size=1)

    return objects


def generate_empties(amount, size):
    empty_objects = []
    for cur in range(amount):
        bpy.ops.object.empty_add(type='ARROWS', radius=size, align='WORLD', location=[0, 0, 0], rotation=[0, 0, 0],
                                 scale=[1, 1, 1])
        tmp_obj = bpy.data.objects['Empty']
        tmp_obj.name = 'Retarget_{}'.format(cur)
        empty_objects.append(tmp_obj)

    return empty_objects


# setting scene frame rate
def add_scene_properties(data):
    m_scene = bpy.context.scene
    scene_frames = len(data)
    if m_scene.frame_end < scene_frames:
        m_scene.frame_end = scene_frames
    return m_scene


def get_obj_blend_shape_ref(obj):
    keys = obj.data.shape_keys.key_blocks
    return keys
