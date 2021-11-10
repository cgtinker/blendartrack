from utils.blend import keyframe, scene, reference
from utils.custom_data import iCustomData
from utils.mapping import BlendShapeMapping


class BlendShapeModel(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.title = title
        self.batch = batch

        self.model = []

    def initialize(self):
        for data in self.json_data[self.title]:
            frame = data['frame']  # receiving frame reference
            blend_shapes = []  # blend shape array at a frame
            for i in range(len(data['blendShapes'])):
                # getting shape key values / titles
                m_blend_shape = BlendShape(data['blendShapes'][i]['shapeKey'], data['blendShapes'][i]['value'])
                blend_shapes.append(m_blend_shape)
            tmp = BlendShapeData(blend_shapes, frame)
            self.model.append(tmp)  # adding blend shapes to the blend shape data array

    def generate(self):
        pass

    def animate(self):
        if self.batch:
            print("hi")
            
        else:
            active_scene = scene.set_scene_frame_end(self.model)
            objects = reference.get_selected_objects(1)
            print("importing blend shape model")

            if len(objects) == 1:
                obj = objects[0]  # currently only enabling import for one selected obj
                keys = reference.get_obj_blend_shape_ref(obj)  # getting stored blend shapes
                ref_dict = BlendShapeMapping.create_blend_shape_mapping(keys)  # reference for shape key import

                for data in self.model:
                    data.init_frame(active_scene)
                    data.keyframe_shape_keys(obj, ref_dict)
            else:
                print('more than one or no object selected')

    def structure(self):
        pass


class BlendShapeData:
    def __init__(self, blend_shapes, frame):
        self.blend_shapes = blend_shapes
        self.frame = frame

    def init_frame(self, scene):
        keyframe.init_keyframe(self.frame, scene)
        print("retargeting blend shape data at frame ", self.frame, end='\r')

    def keyframe_shape_keys(self, obj, ref_dict):
        for i in range(len(self.blend_shapes)):
            index = ref_dict[self.blend_shapes[i].batch]    # get index from reference dict
            self.blend_shapes[i].keyframe_shape_key(index, obj, self.frame)  # setting keyframes

    def print_contents(self):
        print("blend shape data:", self.frame)
        for shape in self.blend_shapes:
            shape.print_shape_content()


class BlendShape:
    def __init__(self, title, value):
        self.title = title
        self.value = value

    def keyframe_shape_key(self, index, obj, frame):
        if index > -1:
            keyframe.set_shape_key(index, self.value, obj, frame)

    def print_shape_content(self):
        print('title: ', self.title, ', value: ', self.value)



