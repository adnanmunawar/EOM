import matplotlib.pyplot as plt
import numpy as np
import math


class Obj():
    def __init__(self):
        self.d0 = 0
        self.v0 = 0
        self.a0 = 0
        self.F0 = 0

        self.d = 0
        self.v = 0
        self.a = 0
        self.F = 0

        self.t = 0
        self.dt = 0.001

        self.m = 1

        self.d_array = []
        self.v_array = []
        self.a_array = []
        self.f_array = []
        self.t_array = []

        self._m_store_trajectory = False

    def eom(self):
        self.v = self.v0 + self.a * self.t
        self.d = self.d0 + 0.5 * (self.v0 + self.v) * self.t
        return self.d

    def apply_force(self, F):
        self.F = F
        self.a = self.F / self.m

    def update(self, dt):
        if self._m_store_trajectory:
            self.trajectory()

        self.d0 = self.d
        self.v0 = self.v
        self.a0 = self.a
        self.F0 = self.F

        self.dt = dt
        self.t = self.t + dt
        d = self.eom()
        return d

    def set_mass(self, m):
        self.m = m

    def store_trajectory(self, check):
        self._m_store_trajectory = check

    def trajectory(self):
        self.d_array.append(self.d0)
        self.v_array.append(self.v0)
        self.a_array.append(self.a0)
        self.f_array.append(self.F0)
        self.t_array.append(self.t)

    def plot_trajectory(self, data_type='Position'):
        if data_type == 'Position':
            Y = self.d_array
        if data_type == 'Velocity':
            Y = self.v_array
        if data_type == 'Acceleration':
            Y = self.a_array
        if data_type == 'Force':
            Y = self.f_array

        plt.plot(self.t_array, Y)
        plt.xlabel('Time')
        plt.ylabel(data_type)
        plt.grid('on')
        plt.show()



def run():

    my_obj = Obj()
    my_obj.apply_force(0.5)
    my_obj.store_trajectory(True)
    dt = 0.001
    for i in range(1,500):
        d = my_obj.update(dt)
        my_obj.apply_force(0)
        print 'Iteration number ', i, ' d =', d

    print my_obj.t_array
    my_obj.plot_trajectory('Acceleration')


if __name__ == '__main__':
    run()