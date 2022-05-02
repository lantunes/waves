import numpy as np
from matplotlib import pyplot as plt

"""
The grad (∇) of a 2D vector field f(x,y) is a 2D rank-2 tensor field, J(x,y).
That is, J maps a point (x, y) to a 2x2 matrix (also known as the Jacobian).
∇f(x,y) = [
 ∂f₁/∂x ∂f₁/∂y  
 ∂f₂/∂x ∂f₂/∂y
]
"""
if __name__ == '__main__':

    X, Y = np.mgrid[-1:8:0.5, -1:8:0.5]

    # f(x,y) = [cos(x), sin(xy)]
    U = np.cos(X)
    V = np.sin(X*Y)

    plt.figure(1)
    ax = plt.axes()
    ax.quiver(X, Y, U, V, color='red')
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(x,y) = [cos(x), sin(xy)]$')

    # ∇f(x,y) = [
    #  -sin(x)    0
    #  y cos(xy)  x cos(xy)
    # ]

    plt.figure(2)
    ax = plt.axes()
    G1_U, G1_V = -np.sin(X), 0
    G2_U, G2_V = Y*np.cos(X*Y), X*np.cos(X*Y)

    # Plot the eigenvectors (scaled by the corresponding eigenvalues) of the matrix at each point.
    E1_U = np.zeros(shape=G1_U.shape)
    E1_V = np.zeros(shape=G1_U.shape)
    E2_U = np.zeros(shape=G1_U.shape)
    E2_V = np.zeros(shape=G1_U.shape)
    NORM = np.zeros(shape=G1_U.shape)
    for i in range(len(G1_U)):
        for j in range(len(G1_U[i])):
            mat = np.array([
                [G1_U[i, j], 0],
                [G2_U[i, j], G2_V[i, j]]
            ])
            eigenvals, eigenvecs = np.linalg.eig(mat)
            first_vec = eigenvals[0] * eigenvecs[:, 0]
            second_vec = eigenvals[1] * eigenvecs[:, 1]
            E1_U[i, j] = first_vec[0]
            E1_V[i, j] = first_vec[1]
            E2_U[i, j] = second_vec[0]
            E2_V[i, j] = second_vec[1]
            NORM[i, j] = np.linalg.norm(mat)
    # ax.quiver(X, Y, E1_U, E1_V, color='green')
    # ax.quiver(X, Y, E2_U, E2_V, color='blue')

    # Alternatively, we can just plot G1_U, G1_V and G2_U, G2_V as quivers directly,
    # The green arrows represent [∂f₁/∂x, ∂f₁/∂y], and the blue arrows represent [∂f₂/∂x, ∂f₂/∂y],
    ax.quiver(X, Y, G1_U, G1_V, color='green')
    ax.quiver(X, Y, G2_U, G2_V, color='blue')

    ax.quiver(X, Y, U, V, color='red', alpha=0.3)
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$\\nabla$f(x,y)')

    fig = plt.figure(3)
    ax = plt.axes()

    # Color the vectors of the field using the Frobenius norm of the corresponding gradient tensors.
    c = (NORM.ravel() - NORM.min()) / NORM.ptp()
    cmap = "hot_r"
    c = getattr(plt.cm, cmap)(c)
    q = ax.quiver(X, Y, U, V, cmap=cmap)
    fig.colorbar(q, shrink=0.7, aspect=20 * 0.7, label='$‖$ $\\nabla f$ $‖_F$')
    q.set_edgecolor(c)
    q.set_facecolor(c)

    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(x,y) = [cos(x), sin(xy)]$')

    plt.show()
