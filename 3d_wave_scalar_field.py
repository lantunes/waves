from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

"""
See:
https://en.wikipedia.org/wiki/Wave_vector
https://en.wikipedia.org/wiki/Bloch%27s_theorem

psi(r) = A * cos(k*r + phi)
A is the amplitude
k is the wave vector
r is the position in space (x, y, z coordinates)
phi is the phase offset
"""

fig = plt.figure()
ax = fig.gca(projection='3d')

# amplitude; gives the intensity of the wave
A = 1
# wave vector; gives the direction and magnitude (i.e. frequency) of wave propagation
k = np.array([3, 1, 0])
# phase offset
phi = 0

def f(r):
    D = np.array([[[np.dot(k, r[h, i, j]) for j in range(len(r))] for i in range(len(r))] for h in range(len(r))])
    return A * np.cos(D + phi)

X, Y, Z = np.mgrid[-1:7:.3, -1:7:.3, -1:7:.3]

R = [[[[X[h][i][j], Y[h][i][j], Z[h][i][j]] for j in range(len(Z))] for i in range(len(Y))] for h in range(len(X))]

R = np.array(R)
V = f(R)

# draw each point of the grid explicitly
s = ax.scatter(X, Y, Z, marker=".", alpha=.5, c=V)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

fig.colorbar(s, shrink=0.7, aspect=20*0.7)

plt.title("$\psi (\mathbf{r})=A\cos(\mathbf{k} \cdot \mathbf{r}+\phi )$ \n{A=%s, k=%s, $\phi$=%s}" % (A, k, phi))
plt.show()