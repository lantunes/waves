from mpl_toolkits import mplot3d
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    X, Y = np.mgrid[-5:5:.1, -5:5:.1]

    expr = sp.sympify("sin(x) + cos(y)")
    fn = sp.lambdify("x,y", expr, "numpy")
    f = fn(X, Y)

    ax.contour3D(X, Y, f, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f')

    ax.plot_surface(X, Y, f, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.title('f(x,y) = sin(x) + cos(y)')
    plt.show()
