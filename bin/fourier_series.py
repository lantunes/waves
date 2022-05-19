import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


"""
Fourier Series

Based on the lecture in: https://www.youtube.com/watch?v=ENrQNiXfaLk
"""
if __name__ == '__main__':
    dx = 0.005
    L = 1  # period length
    X = np.mgrid[dx:1:dx]

    # a step function
    f = np.ones(len(X))
    f[0:len(f)//2] = 0 * f[0:len(f)//2]

    fig, ax = plt.subplots(1, 1)
    ax.plot(X, f, color="k")
    line, = ax.plot([], [], color="r")


    def init():
        line.set_data([], [])
        return line,


    def animate(i):
        m = i+1
        a_0 = (2 / L) * np.sum(np.multiply(f, np.ones(len(X)))) * dx
        f_fs = a_0 / 2

        for n in range(1, m + 1):
            a_n = (2 / L) * np.sum(np.multiply(f, np.cos(2 * np.pi * n * X / L)) * dx)
            b_n = (2 / L) * np.sum(np.multiply(f, np.sin(2 * np.pi * n * X / L)) * dx)
            f_fs = f_fs + a_n * np.cos(2 * np.pi * n * X / L) + b_n * np.sin(2 * np.pi * n * X / L)

        line.set_data(X, f_fs)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=100, interval=20, blit=True)

    plt.ylim(-0.3, 1.3)
    plt.show()
