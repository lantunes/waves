from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

"""
The grad (∇) of a 2D scalar field, f(x,y), is a 2D vector field, g(x, y).
"""
if __name__ == '__main__':

    X, Y = np.mgrid[-3:3:.5, -3:3:.5]
    F = np.sin(X) + np.cos(Y)
    # ∇f(x,y) = [∂f(x,y)/∂x, ∂f(x,y)/∂y]
    U = np.cos(X)  # ∂f(x,y)/∂x
    V = -np.sin(Y)  # ∂f(x,y)/∂y

    plt.figure(1)
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, F, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f')
    ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap='Blues', edgecolor='none', alpha=0.5)
    ax.quiver(X, Y, -3, U, V, 0, length=0.2, color='r')
    ax.set_title('f(x,y) = sin(x) + cos(y)')

    plt.figure(2)
    ax = plt.axes()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.quiver(X, Y, U, V, color='r')
    ax.set_title('$\\nabla$ f(x,y)')

    plt.show()
