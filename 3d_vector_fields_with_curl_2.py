from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

"""
The curl (∇☓) of a 3D vector field, f⃗(x,y,z), is a 3D vector field, g⃗(x,y,z).
"""

X, Y, Z = np.mgrid[-20:20:5, -20:20:5, -20:20:5]

fig = plt.figure(1)
ax = fig.gca(projection='3d')
# f⃗(x,y,z) = [xy, sin(y), 0]
U, V, W = X * Y, np.sin(Y), 0
ax.set_title("[$xy$, $sin(y)$, $0$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.03)

fig = plt.figure(2)
ax = fig.gca(projection='3d')
# ∇☓f⃗(x,y,z) = [0, 0, -x]
U, V, W = 0, 0, -X
ax.set_title("∇☓[$xy$, $sin(y)$, $0$]")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.quiver(X, Y, Z, U, V, W, length=0.2)

plt.show()
