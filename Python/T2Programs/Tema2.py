from sympy import *
import math
from collections import *

def dp3(x,f):
    """
    Calculate the value of f'(x) using progresive differences in 3 nodes.

    Args:
        x ([float]): Nodes.
        f ([float]): Value of f in the nodes.

    Returns:
        The value in the node of f'(x)
    """
    c = x[0]
    h = x[1] - x[0]
    a1 = c + 2*h
    a2 = c + h
    f1 = f[x.index(a1)]
    f2 = f[x.index(a2)]
    f3 = f[0]
    result = (-f1 + 4*f2 - 3*f3)/2*h
    return result

def dc2(x,f):
    """
    Calculate the value of f'(x) using central differences in 2 nodes.

    Args:
        x ([float]): Nodes.
        f ([float]): Value of f in the nodes.

    Returns:
        The value in the node of f'(x)
    """
    c = x[1]
    h = x[1] - x[0]
    a1 = c + h
    a2 = c - h
    f1 = f[x.index(a1)]
    f2 = f[x.index(a2)]
    result = (f1 - f2)/2*h
    return result

def dr3(x,f):
    """
    Calculate the value of f'(x) using regresive differences in 3 nodes.

    Args:
        x ([float]): Nodes.
        f ([float]): Value of f in the nodes.

    Returns:
        The value in the node of f'(x)
    """
    c = x[len(x)-1]
    h = x[1] - x[0]
    a1 = c - 2*h
    a2 = c - h
    a3 = c
    f1 = f[x.index(a1)]
    f2 = f[x.index(a2)]
    f3 = f[x.index(a3)]
    result = (f1 - 4*f2 + 3*f3)/2*h
    return result


def f1d3(x,f):
    """
    Calculate the values of the f'(x) in the provided nodes.

    Args:
        x ([float]): Nodes.
        f ([float]): Value of f in the nodes.

    Returns:
        List with the value in the nodes of f'(x)
    """
    result = []
    h = x[1] - x[0]
    # First node using progresive differences of 3 nodes
    result.append(dp3(x,f))
    # Inner nodes using central differences of 2 nodes
    for i in range(0,len(f)-2):
        result.append(dc2([x[j] for j in range(i,len(x))],[f[j] for j in range(i,len(f))]))
    # Final node using regresive differences of 3 nodes
    result.append(dr3(x,f))
    return result


x = [2.9, 3.0, 3.1, 3.2]
fx = [-4.827866, -4.240058, -3.496909, -2.596792]

print "f'(2.9) dp 3 nodes:", dp3(x, fx)
print "f'(3.0) dc 2 nodes:", dc2(x, fx)
print "f'(3.1) dc 2 nodes:", dc2([x[i] for i in range(1,len(x))],[fx[i] for i in range(1,len(fx))])
print "f'(3.2) dr 3 nodes:", dr3(x,fx)

print f1d3(x,fx)
