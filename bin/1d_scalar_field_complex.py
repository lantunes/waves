import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize


if __name__ == '__main__':
    X, Y = np.mgrid[-3:3.2:0.2, -3:3.2:0.2]
    Z = X + Y*1j

    F = Z**2

    U = np.real(F)
    V = np.imag(F)

    plt.figure(1)
    ax = plt.axes()
    ax.quiver(X, Y, U, V, pivot='mid')

    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('$f(z)$ = $z^2$')

    fig = plt.figure(2)
    ax = plt.axes()

    colors = [[np.linalg.norm([U[i, j], V[i, j]]) for j in range(len(X[0]))] for i in range(len(X))]
    norm = Normalize()
    norm.autoscale(colors)
    colormap = cm.inferno
    colors = np.array(colors).ravel()

    # normalize the arrows, so that they all appear with the same length
    U = U / np.sqrt(U ** 2 + V ** 2)
    V = V / np.sqrt(U ** 2 + V ** 2)
    U[np.isnan(U)] = 0.0
    V[np.isnan(V)] = 0.0

    ax.quiver(X, Y, U, V, color=colormap(norm(colors)), pivot='mid', cmap=colormap)

    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('$f(z)$ = $z^2$')
    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array(colors)
    fig.colorbar(sm, shrink=0.7, aspect=20 * 0.7, label='$‖$ $f$ $‖$')

    plt.show()
