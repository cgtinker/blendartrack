class PoseData:
    def __init__(self, px, py, pz, rx, ry, rz, frame):
        self.px = px
        self.py = pz
        self.pz = py
        self.rx = -rx   # TODO: still requires x mirroring
        self.ry = rz
        self.rz = -ry
        self.frame = frame

    def print_contents(self):
        print("pose data:", 'px', self.px, 'py', self.py, 'pz', self.pz, 'rx', self.rx, 'ry', self.ry, 'rz', self.rz, 'f', self.frame)
