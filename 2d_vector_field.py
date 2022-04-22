import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# X, Y = np.mgrid[:2*np.pi:10j,:2*np.pi:5j]
X, Y = np.mgrid[-1:7:0.5,-1:7:0.5]
U = np.cos(X)
V = np.sin(Y)

# XYpairs = np.dstack([X, Y]).reshape(-1, 2)
# print(XYpairs)

fig, ax = plt.subplots(1,1)
Q = ax.quiver(X, Y, U, V, pivot='mid', color='r', units='inches')

ax.set_xlim(-1, 7)
ax.set_ylim(-1, 7)
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()