from ..execution.objects import KeyframeAssistent
from ..preperation.importing import DecodeJson
import importlib

importlib.reload(KeyframeAssistent)
importlib.reload(DecodeJson)


class BlendShapeData:
    def __init__(self, blend_shapes, frame):
        self.blend_shapes = blend_shapes
        self.frame = frame

    def init_frame(self, scene):
        KeyframeAssistent.init_keyframe(self.frame, scene)
        print("retargeting blend shape data at frame ", self.frame, end='\r')

    def keyframe_shape_keys(self, obj, ref_dict):
        for i in range(len(self.blend_shapes)):
            index = ref_dict[self.blend_shapes[i].title]    # get index from reference dict
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
            KeyframeAssistent.set_shape_key(index, self.value, obj, frame)

    def print_shape_content(self):
        print('title: ', self.title, ', value: ', self.value)


def init_shape_model(json_data, title):
    blend_shape_data = []  # container to store blend shape array data
    for data in json_data[title]:
        frame = data['frame']  # receiving frame reference
        blend_shapes = []  # blend shape array at a frame
        for i in range(len(data['blendShapes'])):
            # getting shape key values / titles
            m_blend_shape = BlendShape(data['blendShapes'][i]['shapeKey'], data['blendShapes'][i]['value'])
            blend_shapes.append(m_blend_shape)
        tmp = BlendShapeData(blend_shapes, frame)
        blend_shape_data.append(tmp)  # adding blend shapes to the blend shape data array
    return blend_shape_data
