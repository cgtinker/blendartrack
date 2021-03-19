from module.mapping import WorldToCameraScreen
from module.execution.objects import KeyframeAssistent
from module.preperation.importing import DecodeJson
import importlib

importlib.reload(KeyframeAssistent)
importlib.reload(DecodeJson)
importlib.reload(WorldToCameraScreen)


class ScreenToWorldData:
    def __init__(self, screen_to_world):
        self.screen_to_world = screen_to_world

    def get_screen_pos_data(self):
        screen_pos_data = self.screen_to_world
        return screen_pos_data

    def print_contents(self):
        for data in self.screen_to_world:
            data.print_contents()


class ScreenToWorldPoint:
    def __init__(self, x, y, z, tx, ty, tz, frame):
        # target screen pos
        self.x = x  # normalized screen pos x
        self.y = y  # normalized screen pos y
        self.z = z  # distance to camera
        # relative world pos
        self.tx = tx
        self.ty = tz
        self.tz = ty

        self.frame = frame

    def print_contents(self):
        print("x", self.x, "y", self.y, "z", self.z, "tx", self.tx, "ty", self.ty, "tz", self.tz, "frame", self.frame)


def init_screen_to_world_model(json_data, title):
    # array to store screen to world data
    screen_to_world = []

    # decoding json
    for data in json_data[title]:
        x, y, z = DecodeJson.get_vert_data(data['screenPos'])
        tx, ty, tz = DecodeJson.get_vert_data(data['objPos'])
        frame = data['frame']
        tmp = ScreenToWorldPoint(x=float(x), y=float(y), z=float(z),
                                 tx=float(tx), ty=float(ty), tz=float(tz), frame=int(frame))
        screen_to_world.append(tmp)
    screen_to_world_model = ScreenToWorldData(screen_to_world=screen_to_world)

    return screen_to_world_model
