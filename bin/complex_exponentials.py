import numpy as np
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
"""
if __name__ == '__main__':

    X = np.mgrid[-1:7:0.1]
    base = np.e
    Z = [base**(x*1j) for x in X]

    Z_real = [z.real for z in Z]
    Z_imag = [z.imag for z in Z]

    F_cos = [np.cos(x * np.log(base)) for x in X]
    F_sin = [np.sin(x * np.log(base)) for x in X]

    plt.figure(1)
    ax = plt.axes()

    ax.plot(X, Z_real, color='blue', label='real')
    ax.plot(X, Z_imag, color='red', label='imaginary')

    ax.plot(X, F_cos, color='blue', label='cos(x ln %s)' % ('e' if base == np.e else base), marker=".")
    ax.plot(X, F_sin, color='red', label='sin(x ln %s)' % ('e' if base == np.e else base), marker=".")

    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_title('$z(x)$ = $%s^{ix}$' % ('e' if base == np.e else base))

    plt.legend()

    plt.show()
