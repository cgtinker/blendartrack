from import_models import iCustomData
from utils.mapping import ProjectionMatrixToCamera
from utils.json import decoder
from utils.blend import reference, name, scene, keyframe
from utils import reference_names


class CameraProjection(iCustomData.ImportModel):
    def __init__(self, json_data, title, batch):
        self.json_data = json_data
        self.title = title
        self.batch = batch

        self.camera_name = reference_names.ar_camera

        self.model = None
        self.camera, self.aspect, self.fit, self.active_scene, self.sensor_width = None, None, None, None, None
        self.scene = None

    def initialize(self):
        camera_projection_data = []
        # camera projection matrix
        for data in self.json_data[self.title]:
            # unities camera projection data
            x, y, a, b, c, d, frame = decoder.get_camera_projection_values(data)
            projection_matrix = CameraProjectionMatrix(x=x, y=y, a=a, b=b, c=c, d=d, frame=frame)
            camera_projection_data.append(projection_matrix)
        # screen resolution
        screen_width, screen_height = decoder.get_device_resolution(self.json_data['resolution'])
        resolution = Resolution(screen_width=screen_width, screen_height=screen_height)
        # camera config
        fps, rec_width, rec_height = decoder.get_camera_config(self.json_data['cameraConfig'])
        camera_config = CameraConfig(fps=fps, rec_width=rec_width, rec_height=rec_height)
        # intrinsics data model
        self.model = CameraProjectionData(camera_projection_data, resolution, camera_config)

    def generate(self):
        self.init_projection_data()

    def animate(self):
        self.sensor_width = self.camera.data.sensor_width
        self.set_proj_data()

    def structure(self):
        pass

    def init_projection_data(self):
        # get scene reference and ref to cam
        self.scene = scene.set_scene_frame_end(self.model.camera_projection)
        # set scene resolution
        scene.set_scene_resolution(
            self.scene,
            self.model.resolution.screen_width,
            self.model.resolution.screen_height)

        # get aspect ratio & sensor width
        self.aspect, self.fit = self.model.get_screen_aspect_ratio()
        if self.batch:
            self.camera = name.get_camera_by_name(self.camera_name)
        else:
            self.camera = reference.get_selected_camera()

    def set_proj_data(self):
        for data in self.model.camera_projection:
            focal_length, frame = data.get_focal_length(
                aspect=self.aspect, fit=self.fit, sensor_width=self.sensor_width
            )
            shift_x, shift_y = data.get_lens_shift(aspect=self.aspect, fit=self.fit)
            keyframe.init_keyframe(scene=self.scene, frame=frame)
            print("retargeting camera projection data at frame ", frame, end='\r')
            keyframe.set_camera_focal_length(focal_length=focal_length, camera=self.camera)
            keyframe.set_camera_lens_shift(shift_x=shift_x, shift_y=shift_y, camera=self.camera)


class CameraProjectionData:
    def __init__(self, camera_projection, resolution, camera_config):
        self.camera_projection = camera_projection
        self.resolution = resolution
        self.camera_config = camera_config

    def get_scene_resolution(self):
        return self.resolution.screen_width, self.resolution.screen_height

    def get_screen_aspect_ratio(self):
        aspect, fit = ProjectionMatrixToCamera.get_screen_aspect_ratio(
            self.resolution.screen_width, self.resolution.screen_height
        )

        return aspect, fit

    def print_contents(self):
        self.resolution.print_contents()
        self.camera_config.print_contents()
        for data in self.camera_projection:
            data.print_contents()


class CameraProjectionMatrix:
    def __init__(self, x, y, a, b, c, d, frame):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.frame = frame

    def get_focal_length(self, aspect, fit, sensor_width):
        focal_length = ProjectionMatrixToCamera.get_camera_focal_length(
            x=self.x, y=self.y, aspect=aspect, fit=fit, sensor_width=sensor_width)
        return focal_length, self.frame

    def get_lens_shift(self, aspect, fit):
        shift_x, shift_y = ProjectionMatrixToCamera.get_lens_shift(
            a=self.a, b=self.b, aspect=aspect, fit=fit)
        return shift_x, shift_y

    def print_contents(self):
        print(
            'x', self.x, 'y', self.y, 'a', self.a,
            'b', self.b, 'c', self.c, 'd', self.d,
            'frame', self.frame
        )


class Resolution:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def print_contents(self):
        print('screen_width: ', self.screen_width, 'screen_height: ', self.screen_height)


class CameraConfig:
    def __init__(self, fps, rec_width, rec_height):
        self.fps = fps
        self.rec_width = rec_height
        self.rec_height = rec_width

    def print_contents(self):
        print('fps: ', self.fps, 'width: ', self.rec_width, 'height: ', self.rec_height)
