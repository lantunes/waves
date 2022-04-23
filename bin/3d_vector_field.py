from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                          np.arange(-0.8, 1, 0.2),
                          np.arange(-0.8, 1, 0.8))

    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
         np.sin(np.pi * z))

    ax.quiver(x, y, z, u, v, w, length=0.1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('f(x,y,z) = [sin($\\pi$x)cos($\\pi$y)cos($\\pi$z), \n'
                 '-cos($\\pi$x)sin($\\pi$y)cos($\\pi$z), \n'
                 '$\\sqrt{2/3}$cos($\\pi$x)cos($\\pi$y)sin($\\pi$z)]')

    plt.show()
