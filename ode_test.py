from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import threading
import time as SysTime



class MotionState():
    def __init__(self):
        self.position = []
        self.velocity = []
        self.time = []
        self.pos_array = []
        self.vel_array = []
        self.t_array = []
        self.lock = threading.Lock()
        self._plot_setup = False
        self.axesp = []
        self.axesv = []
        self._sim_finished = False

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def set_velocity(self, v,t):
        self.velocity = v
        self.time = t
        self.vel_array.append(v)
        self.t_array.append(t)

    def set_position(self, p,t):
        self.position = p
        self.pos_array.append(p)

    def plot_setup(self):
        self._plot_setup = True
        self.axesp, = plt.plot([], [], label='Position')
        self.axesv, = plt.plot([], [], label='Velocity')
        plt.grid(True)
        plt.axis([-1, 100, -15, 15])
        plt.legend([self.axesp, self.axesv], ['Position', 'Velocity'])

    def plot_motion(self):
        if not self._plot_setup:
            self.plot_setup()

        # plt.plot(self.t_array, self.pos_array)
        # plt.plot(self.t_array, self.vel_array)
        self.axesp.set_xdata(self.t_array)
        self.axesp.set_ydata(self.pos_array)
        self.axesv.set_xdata(self.t_array)
        self.axesv.set_ydata(self.vel_array)

        plt.draw()
        plt.pause(0.001)

    def print_motion(self):
        print 'P = ', self.position, 'V = ', self.velocity, 'at time:', self.time

    def set_sim_finished(self, bool):
        self._sim_finished = bool

    def is_sim_finished(self):
        return self._sim_finished

Fmax = 1
m = 0.1
B = 0.1


def my_ode(y, t, ft, Fext, motionObj, sleep_time):
    F = np.interp(t, ft, Fext)
    motionObj.set_position(y[0],t)
    motionObj.set_velocity(y[1],t)
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = (F - B * y[1])/m
    SysTime.sleep(sleep_time)
    return dy


def ode_loop(motionObj):
    t0 = 0.0
    dt = 10.0
    total_time = 5*dt
    tf = t0 + dt
    itrs = 500
    f_res = 10
    y0 = [0, 0]
    tspan = np.linspace(t0, tf, itrs)
    ft = np.linspace(t0, tf, f_res)
    Fext = np.zeros(f_res)
    Fext[1] =  Fmax
    Fext[5] = -Fmax
    sleep_time = (tf - t0) / itrs

    while tf <= total_time:
        print 'Current time span t0: ', t0, ' to tf: ', tf
        y = odeint(my_ode, y0, tspan, args=(ft, Fext, motionObj, sleep_time))
        t0 = tf
        tf += dt
        tspan = np.linspace(t0, tf, itrs)
        ft = np.linspace(t0, tf, f_res)
        sleep_time = (tf - t0) / itrs
        y0 = y[-1]
    print 'Sim Finished, setting sim_finished to True'
    motionObj.set_sim_finished(True)


def main():
    motionObj = MotionState()
    t = threading.Thread(target = ode_loop, args=(motionObj,))
    t.start()

    cnt = 0
    while not motionObj.is_sim_finished():
        motionObj.plot_motion()

if __name__ == '__main__':
    main()


