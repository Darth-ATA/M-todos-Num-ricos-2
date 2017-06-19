import sympy as sp
import math
import numpy as np

def trapecio(f, a, b, N):
    """
    Calculate.
    """
    res = float(0)

    for i in range(1, N-1):
        ai = a + i*(b - a)/N
        res = res + f(ai)

    c = (b - a)/2*N

    return(c*(f(a) + 2*res + f(b)))


def Romberg(f, a, b, tol, numFilas):
    for m in range(0, numFilas):
        R = np.zeros(shape=(numFilas, numFilas))
        R[m, 0] = trapecio(f, a, b, 2**m)

        for k in range(1, m):
            R[m, k] = R[m, k-1] + (R[m, k-1] - R[m-1, k-1])/(4**k - 1)

        print R
        print R[m, m] - R[m, m-1]
        if math.fabs(R[m, m] - R[m, m-1]) < tol:
            return (R[m, m])
    return R

x = sp.Symbol('x')


def f(x):
    return sp.exp(x) + sp.cos(x)

print Romberg(f, 0, math.pi, 0.01, 7)
