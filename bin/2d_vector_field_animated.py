import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

if __name__ == '__main__':

    X, Y = np.mgrid[-1:7:0.5,-1:7:0.5]
    U = np.cos(X)
    V = np.sin(Y)

    fig, ax = plt.subplots(1,1)
    Q = ax.quiver(X, Y, U, V, color='r', units='inches')

    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')


    def update_quiver(num, Q, X, Y):
        U = np.cos(X + num*0.1)
        V = np.sin(Y + num*0.1)
        Q.set_UVC(U,V)
        return Q,


    anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), interval=50, blit=False)
    fig.tight_layout()
    plt.title('f(x,y) = [cos(x), sin(y)]')
    plt.show()
