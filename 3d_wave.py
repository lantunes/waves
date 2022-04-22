from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')


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

# ax.contour3D(V[0, :, :], V[:, 0, :], V[:, :, 0], 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot_surface(X[:, :, 0], Y[:, 0, :], V[29, :, :], rstride=1, cstride=1, cmap='viridis', edgecolor='none')

ax.view_init(azim=-90, elev=-135)

plt.title("$\psi (\mathbf{r})=A\cos(\mathbf{k} \cdot \mathbf{r}+\phi )$ \n{A=%s, k=%s, $\phi$=%s}" % (A, k, phi))
plt.show()