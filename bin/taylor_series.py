import matplotlib.pyplot as plt
import numpy as np
from math import factorial


if __name__ == "__main__":

    def y(x):
        return np.sin(x)

    def series(x, n):
        """
        sin x = x - (x^3 / 3!) + (x^5 / 5!) - (x^7 / 7!) + ...
        """
        result = x
        constant = -1
        denom = 3
        for _ in range(n):
            result += constant * x**denom / factorial(denom)
            constant = -constant
            denom += 2
        return result

    x = np.linspace(0, 5*np.pi, 3001)

    plt.plot(x, y(x), linestyle=":", label='$sin(x)$')
    plt.plot(x, [series(i, 19) for i in x], linewidth=1, label='$x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + ...$')
    plt.legend(loc='lower left')
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.show()