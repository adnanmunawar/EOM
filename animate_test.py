import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.01
        yield 10*math.sin(t), 0

def init():
    plt.axis('equal')
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_xy([0,0])
    cir.center = 0,0.5
    ax.add_patch(line)
    # ax.add_patch(cir)
    return line,

line = plt.Rectangle((0.0, 0.0), 0.25, 0.25)
cir = plt.Circle([0.0,0.5],0.1)
fig, ax = plt.subplots()
ax.grid(True)
prev_t = 0
cur_t = 0
xdata, ydata = [], []

def run(data):
    global prev_t, cur_t
    # update the data
    t, y = data
    prev_t = cur_t
    cur_t = t
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    dt = cur_t - prev_t
    if dt > 0:
        if t >= (((xmax + xmin)/2) + 1):
            xmin += dt
            xmax += dt
    elif dt < 0:
        if t <= (((xmax + xmin)/2) - 1):
            xmin += dt
            xmax += dt
    ax.set_xlim(xmin, xmax)
    ax.figure.canvas.draw()


    line.set_xy([t,y])
    cir.center = t, y+0.5
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()