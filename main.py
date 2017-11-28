from eom import Obj
from collision import Collision
import numpy as np
import threading
from animate_test import PlotPoly
import time as SysTime


class ForceArray():
    def __init__(self):
        self.ft = np.linspace(0,5,50)
        self.f_array = np.zeros([1, 50])
        self.f_array[0, 0] = 10


eom_obj = Obj()
plot_obj = PlotPoly()
itrs = 500
tf = 5.0
t0 = 0.0


def run():
    collision_obj = Collision()
    force_obj = ForceArray()
    eom_obj.set_force_array(force_obj)
    eom_obj.set_collision_check(True)
    eom_obj.store_trajectory(True)
    tspan = [t0, tf]
    dt = (tspan[1] - tspan[0]) / 500
    for i in range(1, itrs):
        [d, v] = eom_obj.update(dt)
        SysTime.sleep(dt)

    eom_obj.set_sim_finished(True)


def main():
    plot_obj.set_data_gen_fcn(eom_obj.get_pos_last())

    t = threading.Thread(target=run)
    t.start()

    plot_obj.create_plot()
    eom_obj.plot_trajectory('All')


if __name__ == '__main__':
    main()
