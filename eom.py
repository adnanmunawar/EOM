import matplotlib.pyplot as plt
import numpy as np
import math


class Obj():
    def __init__(self):
        self.d0 = 0
        self.v0 = 0
        self.a = 0
        self.v = 0
        self.t = 0
        self.dt = 0.001
        self.m = 1;

        self.d_array = []
        self.v_array = []
        self.a_array = []
        self.f_array = []
        self.t_array = []

    def eom(self):
        self.v = self.v0 + self.a * self.t
        d = self.d0 + 0.5 * (self.v0 + self.v) * self.t

        self.v0 = self.v
        self.d0 = d

        return d

    def apply_force(self, F):
        self.a = F / self.m

    def update(self, dt):
        self.dt = dt
        self.t = self.t + dt
        d = self.eom()
        return d

    def set_mass(self, m):
        self.m = m

    def store_trajectory(self, d,v,a, F):
        self.d_array.append(d)
        self.v_array.append(v)
        self.a_array.append(a)
        self.f_array.append(F)
        self.t_array.append(self.t)

    def plot_trajectory(self):
        plt.plot(self.t_array, self.d_array)
        plt.xlabel('Time')
        plt.ylabel('d = Distance')
        plt.show()



def run():

    my_obj = Obj()
    my_obj.apply_force(0.5)
    dt = 0.001
    for i in range(1,500):
        d = my_obj.update(dt)
        my_obj.apply_force(0)
        my_obj.store_trajectory(d, 0, 0, 0)
        print 'Iteration number ', i, ' d =', d

    print my_obj.t_array
    my_obj.plot_trajectory()


if __name__ == '__main__':
    run()