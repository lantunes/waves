from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

"""
The Laplacian (∇²) of a 2D scalar field, f(x,y), is a 2D scalar field, g(x, y).
"""
if __name__ == '__main__':

    X, Y = np.mgrid[-3:3:.5, -3:3:.5]
    F = np.sin(X) + np.cos(Y)
    # ∇²f(x,y) = ∂²f/∂x² + ∂²f/∂y² = -sin(x) - cos(y)
    L = -np.sin(X) - np.cos(Y)

    plt.figure(1)
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, F, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f')
    ax.plot_surface(X, Y, F, rstride=1, cstride=1, cmap='Blues', edgecolor='none', alpha=0.5)
    ax.set_title('f(x,y) = sin(x) + cos(y)')

    plt.figure(2)
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, L, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('$\\nabla^2$ f')
    ax.plot_surface(X, Y, L, rstride=1, cstride=1, cmap='Reds', edgecolor='none', alpha=0.5)
    ax.set_title('$\\nabla^2$ f(x,y)')

    plt.show()
