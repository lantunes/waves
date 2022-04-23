from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X, Y, Z = np.mgrid[-1:7:.7, -1:7:.7, -1:7:.7]

    U = np.cos(X)
    V = np.sin(Y)
    W = -np.cos(Z)

    ax.quiver(X, Y, Z, U, V, W, length=0.4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('f(x,y,z) = [cos(x), sin(y), -cos(z)]')

    plt.show()
