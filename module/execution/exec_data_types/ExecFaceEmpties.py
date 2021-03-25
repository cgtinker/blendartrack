from ..objects import ReferenceObject, KeyframeAssistent, Name
from ..scene import Scene, Collections

import importlib
importlib.reload(ReferenceObject)
importlib.reload(KeyframeAssistent)
importlib.reload(Name)
importlib.reload(Scene)
importlib.reload(Collections)


def animate_empties(batch, model, parent_name, empty_col):
    active_scene, parent = init_face_mesh_empties(model, batch, parent_name)
    # generating empties
    reference_objects = ReferenceObject.generate_empties((len(model[0].vertices)), size=0.0025)
    # key framing empties
    for data in model:
        # data.init_frame(active_scene)
        KeyframeAssistent.init_keyframe(data.frame, active_scene)
        for i in range(len(data.vertices)):
            if data.vertices:
                pos = data.vertices[i].get_pos()
                KeyframeAssistent.set_pos_keyframe(
                    pos[0], pos[1], pos[2], reference_objects[i])
    # setting parent
    for obj in reference_objects:
        obj.parent = parent

    Collections.add_list_to_collection(reference_objects, empty_col)
    Scene.disable_relation_lines()


def init_face_mesh_empties(model, batch, parent_name):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        parent = Name.get_object_by_name(name=parent_name)
    else:
        parent = ReferenceObject.generate_empty_at(
            px=0, py=0, pz=0, size=1, name=parent_name)

    return active_scene, parent