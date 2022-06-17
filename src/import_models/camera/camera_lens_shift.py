from .. import iCustomData
from ...utils import reference_names
from ...utils.blend import keyframe, scene, objects
from ...utils.json import decoder
from ...utils.mapping import WorldToCameraScreen


class CameraLensShift(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.title = title
        self.batch = batch

        self.model = None
        self.camera = None
        self.scene = None
        self.name = objects.get_active_reference(reference_names.ar_camera)

    def initialize(self):
        # array to store screen to world data
        screen_to_world = []

        # decoding json
        for data in self.json_data[self.title]:
            x, y, z = decoder.get_vert_data(data['screenPos'])
            tx, ty, tz = decoder.get_vert_data(data['objPos'])
            frame = data['frame']
            tmp = ScreenToWorldPoint(x=float(x), y=float(y), z=float(z),
                                     tx=float(tx), ty=float(ty), tz=float(tz), frame=int(frame))
            screen_to_world.append(tmp)
        self.model = ScreenToWorldData(screen_to_world=screen_to_world)

    def generate(self):
        if self.batch:
            self.camera = objects.get_camera_by_name(self.name)
        else:
            self.camera = objects.get_selected_camera()

    def animate(self):
        self.scene = scene.set_scene_frame_end(self.model.get_screen_pos_data())
        for data in self.model.screen_to_world:
            # Todo: fix shift err
            self.set_lens_shift(data)
            pass

    def structure(self):
        pass

    def set_lens_shift(self, data):
        keyframe.init_keyframe(frame=data.frame, scene=self.scene)
        if data.z > 0:
            shift_x, shift_y = WorldToCameraScreen.world_to_camera_screen_space(
                scene=self.scene, camera=self.camera, px=data.tx, py=data.ty, pz=data.tz,
                aim_x=data.x, aim_y=data.y
            )
            keyframe.set_camera_lens_shift(shift_x=shift_x, shift_y=shift_y, camera=self.camera)


class ScreenToWorldData:
    def __init__(self, screen_to_world):
        self.screen_to_world = screen_to_world

    def get_screen_pos_data(self):
        screen_pos_data = self.screen_to_world
        return screen_pos_data

    def __repr__(self):
        txt = []
        for data in self.screen_to_world:
            txt.append(data.__repr__())
        return txt


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

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}, z: {self.z}\n' \
               f'tx: {self.tx}, ty: {self.ty}, tz: {self.tz}\n' \
               f'frame: {self.frame}'
