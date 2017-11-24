import math


class Collision():
    def __init__(self):
        self.F = 0
        self.wx = 1
        self.K = 100
        self.epsilon = 0.001
        self.ForceCap = 50
        pass

    def force_cap(self):
        if math.fabs(self.F) > self.ForceCap:
            self.F = (math.fabs(self.F) / self.F) * self.ForceCap

    def compute_collision(self, d):
        if d - self.wx >= 0:
            self.F = self.K * (d - self.wx)
            self.force_cap()
            return self.F
        else:
            return 0
