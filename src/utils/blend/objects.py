import bpy
from mathutils import Vector


def get_objects():
    return bpy.data.objects


def is_camera(obj):
    if obj.type == "CAMERA":
        return True
    return False


def is_mesh(obj):
    if obj.type == "MESH":
        return True
    return False


def deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)


def set_obj_active(obj):
    bpy.context.view_layer.objects.active = obj


def get_object(name):
    return bpy.data.objects[name]


def refresh_objects(objs, frame, scene):
    scene.frame_current = frame
    for obj in objs:
        obj.update_tag(refresh={'OBJECT'})
    scene.update_android()


def update_data_tag(obj):
    obj.update_tag(refresh={'DATA'})


def add_copy_location_constraint(obj, target_obj, use_offset):
    constraint = obj.constraints.new('COPY_LOCATION')
    constraint.target = target_obj
    constraint.use_offset = use_offset


def add_copy_rotation_constraint(obj, target_obj, invert_y, use_offset=False):
    constraint = obj.constraints.new('COPY_ROTATION')
    constraint.target = target_obj
    if invert_y:
        constraint.invert_y = True
    if use_offset:
        constraint.mix_mode = 'ADD'


def get_objects_with_name(name):
    objects = bpy.data.objects
    object_names = []

    for o in objects:
        object_names.append(o.name)

    objects_with_name = []
    for n in object_names:
        if name in n:
            objects_with_name.append(name)

    return objects_with_name


def get_object_by_name(name, size=1):
    m_object = bpy.data.objects.get(name)
    if m_object:
        return m_object
    else:
        m_object = generate_empty_at(px=0, py=0, pz=0, size=size, name=name)
        return m_object


def get_camera_by_name(name):
    camera = bpy.data.objects.get(name)
    if camera:
        return camera
    else:
        camera = create_new_camera(name)
        return camera


def is_name_available(name):
    ref_name = bpy.data.objects.get(name)
    if ref_name:
        return True
    else:
        return False


def set_reference_name(name):
    named_objects = get_objects_with_name(name)
    m_name = name + str(len(named_objects))
    return m_name


def get_active_reference(name):
    m_objects = get_objects_with_name(name)
    m_name = str(name + str(len(m_objects) - 1))
    return m_name


def is_object_selected():
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


def generate_empties(amount, size):
    empty_objects = []
    for cur in range(amount):
        obj = get_object_by_name(f'FaceEmpty_{cur}', size)
        # obj = bpy.data.objects.new('FaceEmpty_{}'.format(cur), None)
        # bpy.context.scene.collection.objects.link(obj)
        #
        # obj.empty_display_size = size
        # obj.empty_display_type = 'ARROWS'

        empty_objects.append(obj)

    return empty_objects


def generate_empty_at(px, py, pz, size, name):
    obj = bpy.data.objects.new(name, None)
    bpy.context.scene.collection.objects.link(obj)
    obj.empty_display_size = size
    obj.empty_display_type = 'ARROWS'
    obj.location = Vector((px, py, pz))
    return obj


def get_obj_blend_shape_ref(obj):
    keys = obj.data.shape_keys.key_blocks
    return keys


def create_new_camera(name):
    camera_data = bpy.data.cameras.new(name=name)
    camera_object = bpy.data.objects.new(name, camera_data)
    bpy.context.scene.collection.objects.link(camera_object)
    return camera_object


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