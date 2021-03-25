from ..objects import ReferenceObject
from ..scene import Scene
from ...mapping import BlendShapeMapping
from importlib import reload

reload(ReferenceObject)
reload(Scene)
reload(BlendShapeMapping)


def exec_keys(batch, model):
    if batch:
        print("hi")
    else:
        active_scene = Scene.set_scene_frame_end(model)
        objects = ReferenceObject.get_selected_objects(1)
        print("importing blend shape model")

        if len(objects) == 1:
            obj = objects[0]  # currently only enabling import for one selected obj
            keys = ReferenceObject.get_obj_blend_shape_ref(obj)  # getting stored blend shapes
            ref_dict = BlendShapeMapping.create_blend_shape_mapping(keys)  # reference for shape key import

            for data in model:
                data.init_frame(active_scene)
                data.keyframe_shape_keys(obj, ref_dict)
        else:
            print('more than one or no object selected')