from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    A = 1
    k = np.array([3, 1])
    phi = 0

    def f(r):
        D = np.array([[np.dot(k, r[i, j]) for j in range(len(r))] for i in range(len(r))])
        return A * np.cos(D + phi)

    all_x = np.linspace(0, 6, 30)
    all_y = np.linspace(0, 6, 30)

    X, Y = np.meshgrid(all_x, all_y)

    R = [[[X[i][j], Y[i][j]] for j in range(len(Y))] for i in range(len(X))]

    R = np.array(R)
    Z = f(R)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('$\psi$')

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    plt.title('$\psi (\mathbf{r})=A\cos(\mathbf{k} \cdot \mathbf{r}+\phi )$ \n{A=%s, k=%s, $\phi$=%s}' % (A, k, phi))
    plt.show()
