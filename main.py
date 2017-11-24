from eom import Obj
from collision import Collision
import matplotlib.pyplot as plt


def run():
    my_obj = Obj()
    collision_obj = Collision()
    my_obj.apply_force(500)
    my_obj.store_trajectory(True)
    dt = 0.001
    for i in range(1,500):
        [d, v] = my_obj.update()
        F = collision_obj.compute_collision(d)
        my_obj.apply_force(-F)

    my_obj.plot_trajectory('Position')

if __name__ == '__main__':
    run()