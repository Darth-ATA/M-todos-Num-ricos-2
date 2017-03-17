from sympy import *
import math
from collections import *

x = Symbol('x')

'''
Implements the bisection method for the root aproximation of a function.
    @param f: function to calculate the root.
    @param a: minimum of the interval.
    @param b: maximum of the interval.
    @param tol: maximum error permitted.
    @param n: maximum iterations permitted.
'''
def Bisection (f, a1, b1, tol):
    # The interval don't satisfy Bolzano condition
    if f(a1) * f(b1) > 0:
        return "Invalid interval"

    # It beats the desired error.
    if tol >= (b1 - a1)/2:
        return (b1 + a1)/2

    Result = namedtuple('Result',['x','n'])
    a = a1
    b = b1

    m = 1
    while tol <= (b - a)/2**(m+1):
        x = (b + a)/2
        # Founds the interval needed.
        if f(a) * f(x) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x

        m += 1

    r=Result(x,m)
    return r

'''
Implements the Regula Falsi method for the root aproximation of a function.
    @param f: function to calculate the root.
    @param a: minimum of the interval.
    @param b: maximum of the interval.
    @param n: maximum iterations permitted.
'''
def RegulaFalsi(f, a1, b1, n):
    # The interval don't satisfy Bolzano condition
    if f(a1) * f(b1) > 0:
        return "Invalid interval"

    a = a1
    b = b1
    m = 1
    while m < n :
        x = b - ((b - a) * f(b))/(f(b) - f(a))

        # Founds the interval needed.
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x

        m += 1
    return x

'''
Implements the Secant method for the root aproximation of a function.
    @param f: function to calculate the root.
    @param x0: number.
    @param x1: number.
    @param tol: maximum error permitted.
    @param n: maximum iterations permitted.
'''
def Secant(f, x0, x1, tol, n):
    m = 1

    x2 = x1 - ((x1 - x0) * f(x1))/(f(x1) - f(x0))
    while tol <= abs(x2 - x1) and m < n :
        x0 = x1
        x1 = x2

        x2 = x1 - ((x1 - x0) * f(x1))/(f(x1) - f(x0))

        m += 1

    return x2


def NewhtonRhapson(f, x0, tol, n):
    '''
    Implements the Newthon-Rhapson method for the root aproximation of a function.
        @param f: function to calculate the root.
        @param x0: initial aproximation.
        @param tol: maximum error permitted.
        @param n: maximum iterations permitted.
    '''
    m = 1

    df = lambda X: diff(f(x),x).evalf(subs={x:X})
    print df(x0)

    x1 = x0 - f(x0)/df(x0)
    while tol <= abs(x1 - x0) and m < n :
        x0 = x1

        x1 = x0 - f(x0)/df(x0)

        m += 1

    return x1

"""
Implements the Horner method
"""

def Horner(pol, x0):
    """
    Implements the Horner aproximation method for calculate the value of p(x0) and p'(x0).
        Args:
            pol: polynomial to calculate the aproximation.
            x0: value.
        Return:
            (r,r1): values of the polynomial and its diff.
    """
    ePol = pol.expand()
    n = degree(ePol)
    a = ePol.all_coeffs()
    b = [x for x in a]

    for k in range(1, n+1):
        b[k] = a[k] + b[k-1]*x0

    r = b[n]

    c = [x for x in b]
    for k in range(1, n+1):
        c[k] = b[k] + c[k-1]*x0

    r1 = c[n-1]
    return (r,r1)
