from sympy import *
from Tema1 import *
import collections
x = Symbol('x')

def f(x):
    return exp(x) - 3

x = Bisection(f, float(0), float(2), float(10**(-20)))

print "Bisection result: ", x.x , "iteraciones", x.n

x = RegulaFalsi(f, float(0), float(2), 25)

print "Regula Falsi result: ", x

x = Secant(f, float(0), float(2), float(10**(-20)), 25)

print "Secant result: ", x

x = NewhtonRhapson(f, float(0), float(10**(-20)), 25)

print "Newthon-Rhapson result: ", x
