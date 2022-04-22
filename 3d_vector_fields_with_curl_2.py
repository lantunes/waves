from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

"""
The curl (∇☓) of a 3D vector field, f⃗(x,y,z), is a 3D vector field, g⃗(x,y,z).
"""

X, Y, Z = np.mgrid[-2:2:.5, -2:2:.5, -2:2:.5]

fig = plt.figure(1)
ax = fig.gca(projection='3d')
# f⃗(x,y,z) = [y, -x, 0]
U, V, W = Y, -X, 0
ax.set_title("[$y$, $-x$, $0$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.3)

fig = plt.figure(2)
ax = fig.gca(projection='3d')
# ∇☓f⃗(x,y,z) = [0, 0, -2]
U, V, W = 0, 0, -2
ax.set_title("∇☓[$y$, $-x$, $0$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.2)


X, Y, Z = np.mgrid[-3:3:.5, -3:3:.5, -3:3:.5]

fig = plt.figure(3)
ax = fig.gca(projection='3d')
# f⃗(x,y,z) = [y/(x^2 + y^2), -x/(x^2 + y^2), 0]
U, V, W = Y/((X**2) + (Y**2)), -X/((X**2) + (Y**2)), 0
ax.set_title("[$y/(x^2 + y^2)$, $-x/(x^2 + y^2)$, $0$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.6)

# apparently, ∇☓[y/(x^2 + y^2), -x/(x^2 + y^2), 0] = [0, 0, 0]

plt.show()
