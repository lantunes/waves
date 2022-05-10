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

    X, Y = np.mgrid[-2:2.3:0.3, -2:2.3:0.3]

    # f(x,y) = [-y/sqrt(x^2 + y^2), x/sqrt(x^2 + y^2)]
    U = -Y / np.sqrt(X ** 2 + Y ** 2)
    V = X / np.sqrt(X ** 2 + Y ** 2)

    plt.figure(1)
    ax = plt.axes()
    ax.quiver(X, Y, U, V, color='red', pivot='mid')
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-2.3, 2.3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(x,y) = [\\frac{-y}{\\sqrt{x^2 + y^2}}, \\frac{x}{\\sqrt{x^2 + y^2}}]$')

    # ∇f(x,y) = [
    #   xy/(x^2 + y^2)^(3/2)   -x^2/(x^2 + y^2)^(3/2)
    #   y^2/(x^2 + y^2)^(3/2)  -xy/(x^2 + y^2)^(3/2)
    # ]
    G1_U, G1_V = (X*Y)/np.power((X**2 + Y**2), 3/2), -X**2/np.power((X**2 + Y**2), 3/2)
    G2_U, G2_V = Y**2/np.power((X**2 + Y**2), 3/2), -X*Y/np.power((X**2 + Y**2), 3/2)

    NORM = np.zeros(shape=G1_U.shape)
    for i in range(len(G1_U)):
        for j in range(len(G1_U[i])):
            mat = np.array([
                [G1_U[i, j], G1_V[i, j]],
                [G2_U[i, j], G2_V[i, j]]
            ])
            NORM[i, j] = np.linalg.norm(mat)

    fig = plt.figure(2)
    ax = plt.axes()

    # Color the vectors of the field using the Frobenius norm of the corresponding gradient tensors.
    c = (NORM.ravel() - NORM.min()) / NORM.ptp()
    cmap = "hot_r"
    c = getattr(plt.cm, cmap)(c)
    q = ax.quiver(X, Y, U, V, cmap=cmap, pivot='mid')
    fig.colorbar(q, shrink=0.7, aspect=20 * 0.7, label='$‖$ $\\nabla f$ $‖_F$')
    q.set_edgecolor(c)
    q.set_facecolor(c)

    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-2.3, 2.3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('$f(x,y) = [\\frac{-y}{\\sqrt{x^2 + y^2}}, \\frac{x}{\\sqrt{x^2 + y^2}}]$')

    plt.show()
