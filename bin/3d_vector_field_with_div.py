from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

"""
The div (∇•) of a 3D vector field, f(x,y,z), is a 3D scalar field, g(x,y,z).
"""
if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X, Y, Z = np.mgrid[-1:7:.7, -1:7:.7, -1:7:.7]

    # f(x,y,z) = [cos(x), sin(y), -cos(z)]
    U = np.cos(X)
    V = np.sin(Y)
    W = -np.cos(Z)

    # ∇•f(x,y,z) = -sin(x) + cos(y) + sin(z)
    DIV = -np.sin(X) + np.cos(Y) + np.sin(Z)

    # draw each point of the grid explicitly
    s = ax.scatter(X, Y, Z, marker='.', c=DIV)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('f(x,y,z) = [cos(x), sin(y), -cos(z)]')

    ax.quiver(X, Y, Z, U, V, W, length=0.4, alpha=0.3, color='gray')

    fig.colorbar(s, shrink=0.7, aspect=20*0.7, label='$\\nabla \cdot$ f')

    plt.show()
