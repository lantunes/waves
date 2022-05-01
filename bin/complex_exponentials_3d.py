import numpy as np
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt


"""
A complex number number in Python is represented by the type `complex`. A complex number can be declared 
by appending `j` to a number:
>> z = 3j
>> z
3j
>> z = 2+3j
>> z
(2+3j)

A complex number can also be initialized in Python using the `complex` constructor:
>> z = complex(2,3)
>> z
(2+3j)

A complex number in Python has the `real` and `imag` properties:
>> z.real
2.0
>> z.imag
3.0

It also has the `conjugate()` function:
>> z.conjugate()
(2-3j)

The module `cmath` has functions that work with complex numbers:
>> import cmath
>> cmath.exp(3j)
(-0.9899924966004454+0.1411200080598672j)

In general, when a real number, `x`, is raised to the power of an imaginary number, `a+ib`, the result 
is an imaginary number `z`:
x^(a+ib) = x^a * (cos(b ln x) + isin(b ln x)) 
"""
if __name__ == '__main__':

    A, B = np.mgrid[0:2:0.2, -1:7:0.1]
    base = np.e
    Z = [[base**(complex(A[i][j], B[i][j])) for j in range(len(A[i]))] for i in range(len(A))]

    Z_real = np.array([[Z[i][j].real for j in range(len(Z[i]))] for i in range(len(Z))])
    Z_imag = np.array([[Z[i][j].imag for j in range(len(Z[i]))] for i in range(len(Z))])

    F_cos = np.array([[base**A[i][j] * np.cos(B[i][j]*np.log(base)) for j in range(len(A[i]))] for i in range(len(A))])
    F_sin = np.array([[base**A[i][j] * np.sin(B[i][j]*np.log(base)) for j in range(len(A[i]))] for i in range(len(A))])

    plt.figure(1)
    ax = plt.axes(projection='3d')
    ax.contour3D(A, B, Z_real, 150, cmap='Blues')
    ax.contour3D(A, B, Z_imag, 150, cmap='Reds')

    ax.plot_wireframe(A, B, F_cos, color='blue', alpha=0.2)
    ax.plot_wireframe(A, B, F_sin, color='red', alpha=0.2)

    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('z')
    ax.set_title('$z(a,b)$ = $%s^{a+ib}$' % ('e' if base == np.e else base))

    plt.figure(2)
    ax = plt.axes(projection='3d')
    ax.plot3D(Z_real[0], Z_imag[0], B[0], label='$z(b)$')
    ax.set_xlabel('$Re(z)$')
    ax.set_ylabel('$Im(z)$')
    ax.set_zlabel('b')
    ax.set_title('$z(b)$ = $%s^{ib}$' % ('e' if base == np.e else base))
    ax.legend()


    plt.show()
