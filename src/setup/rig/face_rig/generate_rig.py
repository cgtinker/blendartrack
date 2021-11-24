from src.setup.rig.face_rig import add_face_rig
from src.setup.rig.face_rig.align_rig import apply_transforms


class FaceRigGenerator():
    def __init__(self):
        self.name = "face_base_rig"
        self.obj = apply_transforms.select_object(self.name)
        pass

    def add_rig(self):
        add_face_rig.add(self.name)
        apply_transforms.apply_transforms_to_object(self.obj)
