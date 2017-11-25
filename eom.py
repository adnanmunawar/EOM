import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from collision import Collision
import math


class Obj():
    def __init__(self):
        self.d0 = 0
        self.v0 = 0

        self.d = 0
        self.v = 0
        self.a = 0
        self.F = 0

        self.t = 0
        self.dt = 0.001

        self.m = 0.1
        self.B = 0.1

        self.d_array = []
        self.v_array = []
        self.a_array = []
        self.f_array = []
        self.t_array = []
        self.fext_array = []

        self._m_store_trajectory = False
        self._f_array_set = False
        self._compute_collision = False
        self.Col_obj = Collision()

    def dynamics(self):
        pass

    def apply_force(self, F):
        self.F = F

    def set_force_array(self, force_array):
        self.fext_array = force_array
        self._f_array_set = True

    def set_collision_check(self, bool):
        self._compute_collision = bool

    def update_force(self):
        if self._f_array_set:
            Fext1 = np.interp(self.t, self.fext_array.ft, self.fext_array.f_array[0])
        if self._compute_collision:
            Fext2 = self.Col_obj.compute_collision(self.d)

        self.F = Fext1 - Fext2

    def update(self, dt = 0.001):

        self.d0 = self.d
        self.v0 = self.v

        if self._m_store_trajectory:
            self.trajectory()

        self.update_force()

        self.dt = dt
        self.t += self.dt
        return self.eom()

    def eom(self):
        self.a = (self.F - self.B * self.v) / self.m
        self.v = self.v0 + self.a * self.dt
        self.d = self.d0 + (0.5 * (self.v0 + self.v) * self.dt)
        return self.d, self.v

    def set_mass(self, m):
        self.m = m

    def store_trajectory(self, check):
        self._m_store_trajectory = check

    def trajectory(self):
        self.d_array.append(self.d0)
        self.v_array.append(self.v0)
        self.a_array.append(self.a)
        self.f_array.append(self.F)
        self.t_array.append(self.t)

    def plot_trajectory(self, data_type='Position'):
        if data_type == 'Position':
            Y = [self.d_array]
        if data_type == 'Velocity':
            Y = [self.v_array]
        if data_type == 'Acceleration':
            Y = [self.a_array]
        if data_type == 'Force':
            Y = [self.f_array]
        if data_type == 'All':
            Y = [self.d_array, self.v_array]

        for i in range(0, len(Y)):
            plt.plot(self.t_array, Y[i])

        plt.xlabel('Time')
        plt.ylabel(data_type)
        plt.grid('on')
        plt.show()

    def plot_time(self):
        plt.plot(self.t_array)
        plt.show()
