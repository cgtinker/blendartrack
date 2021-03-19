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

    def anchor_screen_pos_to_camera(self, scene, camera):
        for data in self.screen_to_world:
            data.world_to_screen_shift(scene=scene, camera=camera)

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

    def world_to_screen_shift(self, scene, camera):
        KeyframeAssistent.init_keyframe(scene=scene, frame=self.frame)
        if self.z > 0:
            shift_x, shift_y = WorldToCameraScreen.world_to_camera_screen_space(
                scene=scene, camera=camera, px=self.tx, py=self.ty, pz=self.tz,
                aim_x=self.x, aim_y=self.y
            )
            KeyframeAssistent.set_camera_lens_shift(shift_x=shift_x, shift_y=shift_y, camera=camera)

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
    # px, py, pz = JsonDecoder.get_vert_data(json_data['anchor'])
    screen_to_world_model = ScreenToWorldData(screen_to_world=screen_to_world)

    return screen_to_world_model
