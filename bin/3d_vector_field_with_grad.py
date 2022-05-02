from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


"""
The grad (∇) of a 3D vector field f(x,y,z) is a 3D rank-2 tensor field, J(x,y,z).
That is, J maps a point (x, y, z) to a 3x3 matrix (also known as the Jacobian).
∇f(x,y) = [
 ∂f₁/∂x ∂f₁/∂y ∂f₁/∂z
 ∂f₂/∂x ∂f₂/∂y ∂f₂/∂z
 ∂f₃/∂x ∂f₃/∂y ∂f₃/∂z
]
"""
if __name__ == '__main__':
    np.seterr(invalid='ignore')

    fig = plt.figure(1)
    ax = fig.gca(projection='3d')

    X, Y, Z = np.mgrid[-3:4:1, -3:4:1, -3:4:1]

    # f(x,y,z) = [-x/(x^2+y^2+z^2), -y/(x^2+y^2+z^2), -z/(x^2+y^2+z^2)]
    U = -X / (X**2 + Y**2 + Z**2)
    V = -Y / (X**2 + Y**2 + Z**2)
    W = -Z / (X**2 + Y**2 + Z**2)

    ax.quiver(X, Y, Z, U, V, W, length=1)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_title('$f(x,y,z) = [-x/(x^2+y^2+z^2), -y/(x^2+y^2+z^2), -z/(x^2+y^2+z^2)]$')

    # ∇f(x,y,z) = [
    # -(-x^2+y^2+z^2)/(x^2+y^2+z^2)^2  (2xy)/(x^2+y^2+z^2)^2           (2xz)/(x^2+y^2+z^2)^2
    # (2xy)/(x^2+y^2+z^2)^2            -(x^2-y^2+z^2)/(x^2+y^2+z^2)^2  (2yz)/(x^2+y^2+z^2)^2
    # (2xz)/(x^2+y^2+z^2)^2            (2yz)/(x^2+y^2+z^2)^2            -(x^2+y^2-z^2)/(x^2+y^2+z^2)^2}
    # ]

    fig = plt.figure(2)
    ax = fig.gca(projection='3d')
    G1_U, G1_V, G1_W = -(-X**2+Y**2+Z**2)/(X**2+Y**2+Z**2)**2, (2*X*Y)/(X**2+Y**2+Z**2)**2, (2*X*Z)/(X**2+Y**2+Z**2)**2
    G2_U, G2_V, G2_W = (2*X*Y)/(X**2+Y**2+Z**2)**2, -(X**2-Y**2+Z**2)/(X**2+Y**2+Z**2)**2, (2*Y*Z)/(X**2+Y**2+Z**2)**2
    G3_U, G3_V, G3_W = (2*X*Z)/(X**2+Y**2+Z**2)**2, (2*Y*Z)/(X**2+Y**2+Z**2)**2, -(X**2+Y**2-Z**2)/(X**2+Y**2+Z**2)**2

    # Plot the eigenvectors (scaled by the corresponding eigenvalues) of the matrix at each point.
    E1_U = np.zeros(shape=G1_U.shape)
    E1_V = np.zeros(shape=G1_U.shape)
    E1_W = np.zeros(shape=G1_U.shape)
    E2_U = np.zeros(shape=G1_U.shape)
    E2_V = np.zeros(shape=G1_U.shape)
    E2_W = np.zeros(shape=G1_U.shape)
    E3_U = np.zeros(shape=G1_U.shape)
    E3_V = np.zeros(shape=G1_U.shape)
    E3_W = np.zeros(shape=G1_U.shape)
    NORM = np.zeros(shape=G1_U.shape)
    for i in range(len(G1_U)):
        for j in range(len(G1_U[i])):
            for k in range(len(G1_U[i][j])):
                mat = np.array([
                    [G1_U[i, j, k], G1_V[i, j, k], G1_W[i, j, k]],
                    [G2_U[i, j, k], G2_V[i, j, k], G2_W[i, j, k]],
                    [G3_U[i, j, k], G3_V[i, j, k], G3_W[i, j, k]]
                ])
                mat = np.where(~np.isfinite(mat), 0, mat)
                eigenvals, eigenvecs = np.linalg.eig(mat)
                first_vec = eigenvals[0] * eigenvecs[:, 0]
                second_vec = eigenvals[1] * eigenvecs[:, 1]
                third_vec = eigenvals[2] * eigenvecs[:, 2]
                E1_U[i, j, k] = first_vec[0]
                E1_V[i, j, k] = first_vec[1]
                E1_W[i, j, k] = first_vec[2]
                E2_U[i, j, k] = second_vec[0]
                E2_V[i, j, k] = second_vec[1]
                E2_W[i, j, k] = second_vec[2]
                E3_U[i, j, k] = third_vec[0]
                E3_V[i, j, k] = third_vec[1]
                E3_W[i, j, k] = third_vec[2]
                NORM[i, j, k] = np.linalg.norm(mat)
    # ax.quiver(X, Y, Z, E1_U, E1_V, E1_W, color='green', length=0.6)
    # ax.quiver(X, Y, Z, E2_U, E2_V, E2_W, color='blue', length=0.6)
    # ax.quiver(X, Y, Z, E3_U, E3_V, E3_W, color='red', length=0.6)

    # Color the vectors of the field using the Frobenius norm of the corresponding gradient tensors.
    c = (NORM.ravel() - NORM.min()) / NORM.ptp()
    # delete the entry representing the point (0, 0, 0), since it has length 0 and won't be drawn
    c = np.delete(c, 171)
    # repeat for each body line and two head lines
    c = np.concatenate((c, np.repeat(c, 2)))
    cmap = "hot_r"
    c = getattr(plt.cm, cmap)(c)
    q = ax.quiver(X, Y, Z, U, V, W, length=1, cmap=cmap)
    fig.colorbar(q, shrink=0.7, aspect=20*0.7, label='$‖$ $\\nabla f$ $‖_F$')
    q.set_edgecolor(c)
    q.set_facecolor(c)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('$f(x,y,z) = [-x/(x^2+y^2+z^2), -y/(x^2+y^2+z^2), -z/(x^2+y^2+z^2)]$')

    plt.show()
