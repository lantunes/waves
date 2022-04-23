import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    A = 1
    k = np.array([1, 3, 5])
    phi = 0

    def f(r):
        D = np.array([[[np.dot(k, r[h, i, j]) for j in range(len(r))] for i in range(len(r))] for h in range(len(r))])
        return A * np.cos(D + phi)

    all_x = np.linspace(0, 6, 30)
    all_y = np.linspace(0, 6, 30)
    all_z = np.linspace(0, 6, 30)

    X, Y, Z = np.meshgrid(all_x, all_y, all_z)

    R = [[[[X[h][i][j], Y[h][i][j], Z[h][i][j]] for j in range(len(Z))] for i in range(len(Y))] for h in range(len(X))]

    R = np.array(R)
    V = f(R)

    slice = 2
    # Z_ = V[slice, :, :]
    # x_label = 'x'
    # y_label = 'y'

    # Z_ = V[:, slice, :]
    # x_label = 'x'
    # y_label = 'z'

    Z_ = V[:, :, slice]
    x_label = 'y'
    y_label = 'z'

    fig, ax = plt.subplots()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    im = ax.imshow(Z_, interpolation='bilinear', origin='lower', cmap='gray', extent=(0, 6, 0, 6))

    fig.colorbar(im, orientation='vertical', shrink=0.8)

    plt.title('$\psi (\mathbf{r})=A\cos(\mathbf{k} \cdot \mathbf{r}+\phi )$ \n{A=%s, k=%s, $\phi$=%s} slice=%s' % (A, k, phi, slice))
    plt.show()
