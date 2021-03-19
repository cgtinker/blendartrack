import module.execution.objects.Name
from module.execution.objects import ReferenceObject, KeyframeAssistent
from module.execution.scene import Scene
from module.mapping import VertexAnimation


def exec_face_anim(batch, model):
    print("importing face mesh model")
    geometry = True
    # animate mesh geometry
    if geometry:
        animate_geometry(model)

    # animate empties
    else:
        animate_empties(batch, model)


def animate_empties(batch, model):
    active_scene, parent = init_face_mesh_empties(model, batch)
    # generating empties
    reference_objects = ReferenceObject.generate_empties((len(model[0].vertices)), size=0.01)
    # key framing empties
    for data in model:
        # data.init_frame(active_scene)
        KeyframeAssistent.init_keyframe(data.frame, active_scene)
        for i in range(len(data.vertices)):
            if data.vertices:
                data.vertices[i].key_pos(reference_objects[i])
        # data.key_pos(reference_objects)
    # setting parent
    for obj in reference_objects:
        obj.parent = parent
    # disabling debug lines to parent
    Scene.disable_relation_lines()


def animate_geometry(model):
    mesh = module.execution.objects.Name.get_object_by_name("r_face_mesh")
    frames = []
    positions = []
    for data in model:
        frames.append(data.frame)
        positions.append(data.get_positions())
    VertexAnimation.animate_geometry(mesh, frames, positions)


def init_face_mesh_empties(model, batch):
    active_scene = Scene.set_scene_frame_end(model)

    if batch:
        # finding parent object
        parent = module.execution.objects.Name.get_object_by_name(name="Retarget_Face_Pos")
    else:
        # generating a parent object
        parent = ReferenceObject.generate_empty_at(px=0, py=0, pz=0, size=1, name="Face_Parent")

    return active_scene, parent
