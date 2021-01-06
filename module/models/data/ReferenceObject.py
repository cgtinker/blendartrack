import bpy
from mathutils import Vector


def object_selected():
    objects = len(bpy.context.selected_objects)
    if objects >= 1:
        return True
    else:
        return False


def get_selected_object():
    objects = len(bpy.context.selected_objects)

    if objects >= 1:
        return bpy.context.selected_objects[0]


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


def generate_empty_at(px, py, pz, size, name):
    obj = bpy.data.objects.new(name, None)
    bpy.context.scene.collection.objects.link(obj)
    obj.empty_display_size = size
    obj.empty_display_type = 'ARROWS'
    obj.location = Vector((px, py, pz))
    return obj


# setting scene frame rate
def add_scene_properties(data):
    # getting scene ref & adjusting scene frame end
    m_scene = get_scene_context()
    scene_frames = len(data)
    if m_scene.frame_end != scene_frames:
        m_scene.frame_end = scene_frames
    return m_scene


def get_scene_context():
    m_scene = bpy.context.scene
    return m_scene


def get_obj_blend_shape_ref(obj):
    keys = obj.data.shape_keys.key_blocks
    return keys


def create_new_camera(name):
    camera_data = bpy.data.cameras.new(name=name)
    camera_object = bpy.data.objects.new(name, camera_data)
    bpy.context.scene.collection.objects.link(camera_object)
    return camera_object


def get_camera_by_name(name):
    camera = bpy.data.objects.get(name)
    if camera:
        return camera
    else:
        camera = create_new_camera(name)
        return camera


def get_object_by_name(name):
    m_object = bpy.data.objects.get(name)
    if m_object:
        return m_object
    else:
        m_object = generate_empty_at(px=0, py=0, pz=0, size=1, name="empty")
        return m_object


def get_selected_camera():
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
