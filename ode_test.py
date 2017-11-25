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

    def plot_motion(self):
        pos_axes, = plt.plot(self.t_array, self.pos_array, label='Position')
        vel_axes, = plt.plot(self.t_array, self.vel_array, label='Velocity')
        plt.grid()
        plt.legend([pos_axes, vel_axes], ['Position', 'Velocity'])
        plt.show()

    def print_motion(self):
        print 'P = ', self.position, 'V = ', self.velocity, 'at time:', self.time

Fmax = 1
m = 0.1
B = 0.1


def my_ode(y, t, ft, Fext, motionObj, sleet_time):
    F = np.interp(t, ft, Fext)
    motionObj.set_position(y[0],t)
    motionObj.set_velocity(y[1],t)
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = (F - B * y[1])/m
    # SysTime.sleep(sleet_time)
    return dy


def ode_loop(motionObj):
    t0 = 0.0
    dt = 20.0
    total_time = 100.0
    tf = t0 + dt
    itrs = 50
    f_res = 10
    y0 = [0, 0]
    tspan = np.linspace(t0, tf, itrs)
    ft = np.linspace(t0, tf, f_res)
    Fext = np.zeros(f_res)
    Fext[0] = Fmax
    Fext[5] = -Fmax
    sleep_time = (tspan[1] - tspan[0]) / itrs

    while tf <= total_time:
        # print 'Current time span t0: ', t0, ' to tf: ', tf
        y = odeint(my_ode, y0, tspan, args=(ft, Fext, motionObj, sleep_time))
        t0 = tf
        tf += dt
        tspan = np.linspace(t0, tf, itrs)
        ft = np.linspace(t0, tf, f_res)
        sleep_time = (tspan[1] - tspan[0]) / itrs
        y0 = y[-1]

    motionObj.plot_motion()


def main():
    motionObj = MotionState()
    ode_loop(motionObj)
    # t = threading.Thread(target = ode_loop, args=(motionObj,))
    # t.start()

    # cnt = 0
    # while cnt < 100:
    #     motionObj.print_motion()
    #     cnt += 1
    #     SysTime.sleep(0.1)

if __name__ == '__main__':
    main()


