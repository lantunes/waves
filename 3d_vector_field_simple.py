from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

X, Y, Z = np.mgrid[-1:7:1, -1:7:1, -1:7:1]

# draw each point of the grid explicitly
ax.scatter(X, Y, Z, marker=".", alpha=.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# first 3 arguments are the x, y, and z coordinates of the origin of the arrow
# second 3 arguments are the x, y, and z components of the vector
ax.quiver([0],[0],[0],[1],[1],[0])

plt.show()
