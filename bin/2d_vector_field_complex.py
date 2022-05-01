import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize


"""
f(z, w) = [z^2, w+1/w]
"""
if __name__ == '__main__':

    X, Y = np.mgrid[-3:3.2:0.2, -3:3.2:0.2]
    Z = X + Y * 1j
    W = X + Y * 1j

    F_Z = Z**2
    F_W = W + (1/W)
    F_W[np.isnan(F_W)] = 0.0

    plt.figure(1)
    ax = plt.axes()
    U = np.real(F_Z)
    V = np.real(F_W)
    ax.quiver(X, Y, U, V, color='blue', pivot='mid')
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(z,w)$ = [$z^2$, $w + 1/w$]\nRe(f)')

    fig = plt.figure(2)
    ax = plt.axes()
    colors = [[np.linalg.norm([U[i, j], V[i, j]]) for j in range(len(X[0]))] for i in range(len(X))]
    norm = Normalize()
    norm.autoscale(colors)
    colormap = cm.winter
    colors = np.array(colors).ravel()
    # normalize the arrows, so that they all appear with the same length
    U = U / np.sqrt(U ** 2 + V ** 2)
    V = V / np.sqrt(U ** 2 + V ** 2)
    U[np.isnan(U)] = 0.0
    V[np.isnan(V)] = 0.0
    ax.quiver(X, Y, U, V, color=colormap(norm(colors)), pivot='mid', cmap=colormap)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(z,w)$ = [$z^2$, $w + 1/w$]\nRe(f)')
    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array(colors)
    fig.colorbar(sm, shrink=0.7, aspect=20 * 0.7, label='$‖$ $Re(f)$ $‖$')

    plt.figure(3)
    ax = plt.axes()
    U = np.imag(F_Z)
    V = np.imag(F_W)
    ax.quiver(X, Y, U, V, color='red', pivot='mid')
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(z,w)$ = [$z^2$, $w + 1/w$]\nIm(f)')

    fig = plt.figure(4)
    ax = plt.axes()
    colors = [[np.linalg.norm([U[i, j], V[i, j]]) for j in range(len(X[0]))] for i in range(len(X))]
    norm = Normalize()
    norm.autoscale(colors)
    colormap = cm.autumn
    colors = np.array(colors).ravel()
    # normalize the arrows, so that they all appear with the same length
    U = U / np.sqrt(U ** 2 + V ** 2)
    V = V / np.sqrt(U ** 2 + V ** 2)
    U[np.isnan(U)] = 0.0
    V[np.isnan(V)] = 0.0
    ax.quiver(X, Y, U, V, color=colormap(norm(colors)), pivot='mid', cmap=colormap)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.5, 3.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(z,w)$ = [$z^2$, $w + 1/w$]\nIm(f)')
    sm = cm.ScalarMappable(cmap=colormap, norm=norm)
    sm.set_array(colors)
    fig.colorbar(sm, shrink=0.7, aspect=20 * 0.7, label='$‖$ $Im(f)$ $‖$')

    plt.show()
