from eom import Obj
from collision import Collision
import numpy as np
import matplotlib.pyplot as plt


class ForceArray():
    def __init__(self):
        self.ft = np.linspace(0,5,50)
        self.f_array = np.zeros([1, 50])
        self.f_array[0, 0] = 10


def run():
    my_obj = Obj()
    collision_obj = Collision()
    force_obj = ForceArray()
    my_obj.set_force_array(force_obj)
    my_obj.store_trajectory(True)
    itrs = 500
    tspan = [0.0, 5.0]
    dt = (tspan[1] - tspan[0]) / 500
    print 'Time span (s) ', tspan, ' No. Iterations ', itrs, '  dt ', dt
    for i in range(1, 500):
        [d, v] = my_obj.update(dt)
        F = collision_obj.compute_collision(d)
        my_obj.apply_force(-F)

    my_obj.plot_trajectory('All')

if __name__ == '__main__':
    run()