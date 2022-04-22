from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

X, Y = np.mgrid[-5:5:.1, -5:5:.1]

f = np.sin(X) + np.cos(Y)

ax.contour3D(X, Y, f, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f')

ax.plot_surface(X, Y, f, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

ax.view_init(azim=-90, elev=-135)

plt.title("z = sin(x) + cos(y)")
plt.show()