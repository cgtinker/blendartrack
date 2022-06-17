import bpy


def set_scene_frame_end(data):
    # getting scene ref & adjusting scene frame end
    m_scene = get_scene()
    scene_frames = len(data) - 1
    if m_scene.frame_end != scene_frames:
        m_scene.frame_end = scene_frames
    return m_scene


def get_scene():
    m_scene = bpy.context.scene
    return m_scene


def get_context():
    return bpy.context


def set_scene_resolution(scene, screen_width, screen_height):
    scene.render.resolution_x = int(screen_width)
    scene.render.resolution_y = int(screen_height)


def disable_relation_lines():
    try:
        bpy.context.space_data.overlay.show_relationship_lines = False
    except AttributeError:
        print("attempted to disable relation lines, space text editor object attribute error occured.")


def get_frame_start():
    scn = get_scene()
    return scn.frame_start


def get_frame_end():
    scn = get_scene()
    return scn.frame_end


def set_cursor_location(loc):
    bpy.context.scene.cursor.location = loc


def set_edit_mode():
    bpy.ops.object.mode_set(mode='EDIT')


def set_object_mode():
    bpy.ops.object.mode_set(mode='OBJECT')


def set_pose_mode():
    bpy.ops.object.mode_set(mode='POSE')


def get_user():
    return get_scene.m_cgtinker_blendartrack


def scene(scene):
    scene.refresh()


def reset_timeline():
    print("reset_timeline")
    active_scene = get_scene()
    from . import keyframe
    keyframe.init_keyframe(frame=1, scene=active_scene)


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