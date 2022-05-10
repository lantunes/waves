import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

if __name__ == '__main__':

    X, Y = np.mgrid[-1:7:0.5, -1:7:0.5]

    m = sp.Matrix(["cos(x)", "sin(y)"])
    fn = sp.lambdify("x,y", m, "numpy")
    Z = fn(X, Y)
    U = Z[0][0]
    V = Z[1][0]

    """
    TODO
    >> m.jacobian(["x", "y"])
    Matrix([
    [-sin(x),      0],
    [      0, cos(y)]])
    """

    plt.figure(1)
    ax = plt.axes()
    ax.quiver(X, Y, U, V, color='r')

    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('f(x,y) = [cos(x), sin(y)]')

    plt.show()
