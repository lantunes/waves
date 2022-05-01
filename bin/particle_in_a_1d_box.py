import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.animation as animation


if __name__ == '__main__':
    min_x = -1.97
    max_x = 2.85
    X = np.mgrid[min_x:max_x:0.1]

    A = 1j
    B = 1j
    k = 2
    w = 1
    t = 1

    def psi(A, B, k, X, w, t):
        return (A*np.sin(k*X) + B*np.cos(k*X)) * np.e**(-w*1j*t)

    def make_title(A, B, k, w, t):
        return '$\\psi(x,t)$ = $[A sin(k x) + B cos(k x)]e^{-i \\omega t}$\n' \
               '$A$=%si, $B$=%si, $k$=%s, $\\omega$=%s, $t$=%4.1f' % (A.imag, B.imag, k, w, t)

    Y = psi(A, B, k, X, w, t)
    Y_real = [y.real for y in Y]
    Y_imag = [y.imag for y in Y]

    fig = plt.figure(1)
    ax = plt.axes(projection='3d')

    line_imag, = ax.plot(X, Y_imag, np.zeros(shape=X.shape), color='red', label='imaginary')
    line_real, = ax.plot(X, np.zeros(shape=X.shape), Y_real, color='blue', label='real')
    ax.plot([min_x, max_x], [0, 0], color='black')
    ax.set_xlabel('x')
    ax.set_ylabel('$Im(\\psi)$')
    ax.set_zlabel('$Re(\\psi)$')
    ax.set_ylim3d([-2.0, 2.0])
    ax.set_zlim3d([-2.0, 2.0])
    title = ax.set_title(make_title(A, B, k, w, t), size=10, fontdict={'family': 'monospace'})
    ax.legend()

    T = np.mgrid[0:4*np.pi+0.1:0.1]
    frame = {'index': 0}

    def update_lines(num, line_imag, line_real, title):
        t = T[frame['index']]
        Y = psi(A, B, k, X, w, t)
        Y_real = [y.real for y in Y]
        Y_imag = [y.imag for y in Y]
        line_imag.set_data(X, Y_imag)
        line_imag.set_3d_properties(np.zeros(shape=X.shape))
        line_real.set_data(X, np.zeros(shape=X.shape))
        line_real.set_3d_properties(Y_real)
        frame['index'] = (frame['index']+1) % len(T)
        title.set_text(make_title(A, B, k, w, t))

        return line_imag, line_real, title

    line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=[line_imag, line_real, title],
                                       interval=50, blit=False)

    plt.figure(2)
    ax = plt.axes()
    Y_absolute_squared = [y*y.conjugate() for y in Y]
    # ensure that all the imaginary parts are 0 before we discard them
    assert np.all(np.imag(Y_absolute_squared) == 0.)
    Y_absolute_squared = np.real(Y_absolute_squared)
    ax.plot(X, Y_absolute_squared)
    ax.plot([min_x, max_x], [0, 0], color='black')
    ax.set_xlabel('x')
    ax.set_ylabel('$|\\psi|^2$')
    ax.set_title('$|\\psi(x,t)|^2$')

    plt.show()
