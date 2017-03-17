#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from Tema1 import *
from sympy import *
from collections import *
import math
import numpy as np

#2. Encuentra una aproximación de la raíz cúbica de 52 con un error menor que 10^(-8)
#   mediante el algoritmo de bisección.

def f(x):
    return 3**2 + np.exp(x) - 1

xB=Bisection(f,float(0),float(1),10**(-5))
xR=RegulaFalsi(f,float(0),float(1),10)

print "mediante el metodo de Biseccion", xB
print "mediante el metodo de RegulaFalsi", xR

import matplotlib.pyplot as plt
t1 = np.arange(-5.0,5.0,0.1)

plt.figure()
plt.grid(true)
plt.plot(t1,f(t1),'k')
plt.ylabel('some numbers')
plt.show()
