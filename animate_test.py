import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

class PlotPoly():
    def __init__(self):
        self.shape1 = plt.Rectangle((0.0, 0.0), 0.25, 0.25)
        self.shape2 = plt.Circle([0.0, 0.5], 0.1)
        self.fig, self.ax = plt.subplots()
        self.ax.grid(True)
        self.prev_t = 0
        self.cur_t = 0
        self.prev_y = 0
        self.cur_y = 0
        self.xdata, self.ydata = [], []

    def setup(self):
        plt.axis('equal')
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.set_xlim(0, 10)
        del self.xdata[:]
        del self.ydata[:]
        self.shape1.set_xy([0, 0])
        self.shape2.center = 0, 0.5
        self.ax.add_patch(self.shape1)
        # ax.add_patch(cir)
        return self.shape1,

    def data_gen(self, t=0):
        cnt = 0
        while cnt < 1000:
            cnt += 1
            t += 0.01
            yield 10 * math.sin(t), 1 * math.cos(5 * t)

    def run(self, data):
        # update the data
        t, y = data
        self.prev_t = self.cur_t
        self.prev_y = self.cur_y
        self.cur_t = t
        self.cur_y = y
        self.xdata.append(t)
        self.ydata.append(y)
        self.check_axes_lims(t,y)
        self.shape1.set_xy([t, y])
        self.shape2.set_color('m')
        self.shape2.center = t, y + 0.5
        return self.shape1,

    def check_axes_lims(self, t, y):
        xmin, xmax = self.ax.get_xlim()
        ymin, ymax = self.ax.get_ylim()

        dt = self.cur_t - self.prev_t
        dy = self.cur_y - self.prev_y
        x_center = (xmax + xmin) / 2
        y_center = (ymax + ymin) / 2

        if t < xmin or t > xmax:
            xmin = t - ((xmax - xmin) / 2)
            xmax = t + ((xmax - xmin) / 2)
        if dt > 0 and t >= (x_center + 1):
            xmin += dt
            xmax += dt
        if dt < 0 and t <= (x_center - 1):
            xmin += dt
            xmax += dt

        if y < ymin or y > ymax:
            ymin = y - ((ymax - ymin) / 2)
            ymax = y + ((ymax - ymin) / 2)
        elif dy > 0 and y >= (y_center + 0.7):
            ymin += dy
            ymax += dy
        elif dy < 0 and y <= (y_center - 0.7):
            ymin += dy
            ymax += dy

        self.ax.set_ylim(ymin, ymax)
        self.ax.set_xlim(xmin, xmax)
        self.ax.figure.canvas.draw()

    def create_plot(self):
        ani = animation.FuncAnimation(self.fig, self.run, self.data_gen, blit=False, interval=10,
                                      repeat=False, init_func=self.setup)
        plt.show()

obj = PlotPoly()
obj.create_plot()
