from mpl_toolkits import mplot3d
import sympy as sp
from sympy import print_latex
import numpy as np
import matplotlib.pyplot as plt
import io
from contextlib import redirect_stdout


if __name__ == '__main__':

    # these could be symbols that are constants in the library that could be exported to users
    phi = "φ"
    omega = "ω"
    psi = "Ψ"

    defn = f"{psi}(x,t) = A * cos(k * x - {omega} * t + {phi})"
    constants = {"A": 1, "k": 6, omega: 1, phi: 0}

    fn_sig, fn_def = [s.strip() for s in defn.split("=")]

    expr = sp.sympify(fn_def)

    fn_expr = sp.sympify(fn_sig)

    # substitute in the constants
    expr = expr.subs(constants)
    fn = sp.lambdify(fn_expr.args, expr, "numpy")

    all_x = np.linspace(0, 6, 30)
    all_t = np.linspace(0, 6, 30)

    X, T = np.meshgrid(all_x, all_t)
    Z = fn(X, T)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, T, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('$\psi$')

    ax.plot_surface(X, T, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    ax.view_init(azim=-90, elev=-135)

    with io.StringIO() as buf, redirect_stdout(buf):
        print_latex(expr)
        latex = buf.getvalue().strip()
    plt.title('%s = $%s$ \n{%s}' % (fn_sig, latex, ", ".join(["%s=%s" % (k, v) for k, v in constants.items()])))
    plt.show()
