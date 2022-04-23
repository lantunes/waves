from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    A = 1
    k = 6
    omega = 0
    phi = 0

    def f(x, t):
        return A * np.cos(k * x - omega * t + phi)

    all_x = np.linspace(0, 6, 30)
    all_t = np.linspace(0, 6, 30)

    X, T = np.meshgrid(all_x, all_t)
    Z = f(X, T)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, T, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('$\psi$')

    ax.plot_surface(X, T, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    ax.view_init(azim=-90, elev=-135)

    plt.title('$\psi (x,t)=A\cos(kx-\omega t+\phi )$ \n{A=%s, k=%s, $\omega$=%s, $\phi$=%s}' % (A, k, omega, phi))
    plt.show()
