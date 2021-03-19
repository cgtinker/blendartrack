from module.mapping import ProjectionMatrixToCamera
from module.execution.objects import KeyframeAssistent
from module.preperation.importing import DecodeJson
from module.execution.objects import ReferenceObject
from module.execution.scene import Scene
import importlib

importlib.reload(KeyframeAssistent)
importlib.reload(DecodeJson)
importlib.reload(ReferenceObject)
importlib.reload(ProjectionMatrixToCamera)


class CameraProjectionData:
    def __init__(self, camera_projection, resolution, camera_config):
        self.camera_projection = camera_projection
        self.resolution = resolution
        self.camera_config = camera_config

    def set_scene_resolution(self, scene):
        Scene.set_scene_resolution(
            scene=scene, screen_width=self.resolution.screen_width,
            screen_height=self.resolution.screen_height
        )

    def get_screen_aspect_ratio(self):
        aspect, fit = ProjectionMatrixToCamera.get_screen_aspect_ratio(
            self.resolution.screen_width, self.resolution.screen_height
        )
        
        return aspect, fit

    def set_camera_projection(self, sensor_width, aspect, fit, camera, scene):
        for data in self.camera_projection:
            focal_length, frame = data.get_focal_length(
                aspect=aspect, fit=fit, sensor_width=sensor_width
            )
            shift_x, shift_y = data.get_lens_shift(aspect=aspect, fit=fit)
            KeyframeAssistent.init_keyframe(scene=scene, frame=frame)
            print("retargeting camera projection data at frame ", frame, end='\r')
            KeyframeAssistent.set_camera_focal_length(focal_length=focal_length, camera=camera)
            KeyframeAssistent.set_camera_lens_shift(shift_x=shift_x, shift_y=shift_y, camera=camera)

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


def init_camera_projection_data(json_data, title):
    camera_projection_data = []
    # decoding json
    # camera projection matrix
    for data in json_data[title]:
        # unities camera projection data
        x, y, a, b, c, d, frame = DecodeJson.get_camera_projection_values(data)
        projection_matrix = CameraProjectionMatrix(x=x, y=y, a=a, b=b, c=c, d=d, frame=frame)
        camera_projection_data.append(projection_matrix)
    # screen resolution
    screen_width, screen_height = DecodeJson.get_device_resolution(json_data['resolution'])
    resolution = Resolution(screen_width=screen_width, screen_height=screen_height)
    # camera config
    fps, rec_width, rec_height = DecodeJson.get_camera_config(json_data['cameraConfig'])
    camera_config = CameraConfig(fps=fps, rec_width=rec_width, rec_height=rec_height)
    # intrinsics data model
    intrinsics_model = CameraProjectionData(camera_projection_data, resolution, camera_config)

    return intrinsics_model
