from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

"""
The curl (∇☓) of a 3D vector field, f⃗(x,y,z), is a 3D vector field, g⃗(x,y,z).
"""

X, Y, Z = np.mgrid[-20:20:5, -20:20:5, -20:20:5]

fig = plt.figure(1)
ax = fig.gca(projection='3d')
# f⃗(x,y,z) = [xy, x-z, z^2-y]
U, V, W = X * Y, X - Z, Z**2 - Y
ax.set_title("[$xy$, $x-z$, $z^2-y$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.01)

fig = plt.figure(2)
ax = fig.gca(projection='3d')
# ∇☓f⃗(x,y,z) = [0, 0, 1-x]
U, V, W = 0, 0, 1-X
ax.set_title("∇☓[$xy$, $x-z$, $z^2-y$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.2)


fig = plt.figure(3)
ax = fig.gca(projection='3d')
# g⃗(x,y,z) = [xy, xz, z^2-y]
U, V, W = X * Y, X * Z, Z**2 - Y
ax.set_title("[$xy$, $xz$, $z^2-y$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.01)

fig = plt.figure(4)
ax = fig.gca(projection='3d')
# ∇☓g⃗(x,y,z) = [-x-1, 0, z-x]
U, V, W = -X-1, 0, Z-X
ax.set_title("∇☓[$xy$, $xz$, $z^2-y$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.2)


fig = plt.figure(5)
ax = fig.gca(projection='3d')
# h⃗(x,y,z) = [xy, xz, zy]
U, V, W = X * Y, X * Z, Z * Y
ax.set_title("[$xy$, $xz$, $zy$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.01)

fig = plt.figure(6)
ax = fig.gca(projection='3d')
# ∇☓h⃗(x,y,z) = [z-x, 0, z-x]
U, V, W = Z-X, 0, Z-X
ax.set_title("∇☓[$xy$, $xz$, $zy$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.2)

plt.show()
