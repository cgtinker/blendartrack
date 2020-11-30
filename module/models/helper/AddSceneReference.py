import bpy
from mathutils import Vector


def get_selected_objects(amount):
    objects = len(bpy.context.selected_objects)

    if objects >= 1:
        objects = bpy.context.selected_objects

    else:
        objects = generate_empties(amount, 1)

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


def generate_empty_at(px, py, pz, size):
    obj = bpy.data.objects.new('point', None)
    bpy.context.scene.collection.objects.link(obj)
    obj.empty_display_size = size
    obj.empty_display_type = 'ARROWS'
    obj.location = Vector((px, py, pz))


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


def create_new_camera():
    camera_data = bpy.data.cameras.new(name='Retargeted_Camera')
    camera_object = bpy.data.objects.new('Retargeted_Camera', camera_data)
    bpy.context.scene.collection.objects.link(camera_object)
    return camera_object


def get_scene_camera():
    active_object = bpy.context.selected_objects

    # if selected obj is a camera return it
    if active_object is not None and len(active_object) == 1:
        if active_object[0].type == 'CAMERA':
            return active_object[0]
        else:
            camera = create_new_camera()
            return camera
    # else return a new camera object for intrinsics data mapping
    else:
        camera = create_new_camera()
        return camera


def set_scene_resolution(scene, screen_width, screen_height):
    scene.render.resolution_x = screen_width
    scene.render.resolution_y = screen_height
