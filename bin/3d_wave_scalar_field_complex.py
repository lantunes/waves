from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    # wave vector; gives the direction and magnitude (i.e. frequency) of wave propagation
    k = np.array([3, 1, 0])

    def f(r):
        D = np.array([[[np.dot(k, r[h, i, j]) for j in range(len(r))] for i in range(len(r))] for h in range(len(r))])
        return np.exp(-1j*D)

    X, Y, Z = np.mgrid[-1:7:.3, -1:7:.3, -1:7:.3]

    R = [[[[X[h][i][j], Y[h][i][j], Z[h][i][j]] for j in range(len(Z))] for i in range(len(Y))] for h in range(len(X))]

    R = np.array(R)
    V = f(R)

    fig = plt.figure(1)
    ax = fig.gca(projection='3d')
    # draw each point of the grid explicitly
    s = ax.scatter(X, Y, Z, marker='.', alpha=.5, c=np.real(V), cmap="Blues")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    fig.colorbar(s, shrink=0.7, aspect=20*0.7, label='$Re(\psi (\mathbf{r}))$')
    plt.title('$\psi (\mathbf{r})= e^{-i\mathbf{k} \cdot \mathbf{r}}$ \n{k=%s}' % k)

    fig = plt.figure(2)
    ax = fig.gca(projection='3d')
    # draw each point of the grid explicitly
    s = ax.scatter(X, Y, Z, marker='.', alpha=.5, c=np.imag(V), cmap="Reds")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    fig.colorbar(s, shrink=0.7, aspect=20 * 0.7, label='$Im(\psi (\mathbf{r}))$')
    plt.title('$\psi (\mathbf{r})= e^{-i\mathbf{k} \cdot \mathbf{r}}$ \n{k=%s}' % k)

    plt.show()
