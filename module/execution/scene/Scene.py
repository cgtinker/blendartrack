import bpy


def set_scene_frame_end(data):
    # getting scene ref & adjusting scene frame end
    m_scene = get_scene_context()
    scene_frames = len(data) - 1
    if m_scene.frame_end != scene_frames:
        m_scene.frame_end = scene_frames
    return m_scene


def get_scene_context():
    m_scene = bpy.context.scene
    return m_scene


def set_scene_resolution(scene, screen_width, screen_height):
    scene.render.resolution_x = screen_width
    scene.render.resolution_y = screen_height


def disable_relation_lines():
    bpy.context.space_data.overlay.show_relationship_lines = False
