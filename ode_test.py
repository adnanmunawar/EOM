from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import threading

Fmax = 2
m = 0.1
B = 0.1
time = 50
f_res = 10


class MotionState():
    def __init__(self):
        self.position = []
        self.velocity = []
        self.time = []

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def set_velocity(self, v,t):
        self.velocity = v
        self.time = t

    def set_position(self, p,t):
        self.position = p
        self.time = t

    def print_motion(self):
        print 'P = ', self.position, 'V = ', self.velocity, 'at time:', self.time


def my_ode(y, t, ft, Fext, motionObj):
    F = np.interp(t, ft, Fext)
    motionObj.set_position(y[0],t)
    motionObj.set_velocity(y[1],t)
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = (F - B * y[1])/m
    return dy


def main():
    motionObj = MotionState()
    y0 = [0, 0]
    tspan = np.linspace(0, time, 50)
    ft = np.linspace(0, time, f_res)
    Fext = np.zeros(f_res)
    Fext[0] = Fmax
    Fext[7] = -Fmax
    y = odeint(my_ode, y0, tspan, args=(ft, Fext, motionObj))
    vel_plt, = plt.plot(y[:,1], '-r')
    plt.xlabel('Time')
    pos_plt, = plt.plot(y[:,0], '-g')
    plt.legend([pos_plt, vel_plt], ['Position', 'Velocity'])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()


