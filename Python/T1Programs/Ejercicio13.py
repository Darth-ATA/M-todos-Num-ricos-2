from sympy import *
from Tema1 import *
import collections

print " "

y = Symbol('y')
pol = Poly(2*(y**4) - 3*(y**2) + 3*y - 4, y)

print pol

n = Horner(pol, -2)
print pol(-2)
print "Horner result: ", n
