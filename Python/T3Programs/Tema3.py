import sympy as sp
import math

"""
Ejercicios 05-10-2017
"""

t = sp.Symbol('t')
y = sp.Symbol('y')


def Euler(y0, f, h, a, b):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h*f(tj, u[i]))
        i += 1
        tj += h
    return u


def ExactValueTableEuler(y0, f, h, a, b, F):
    u = Euler(y0, f, h, a, b)
    row = ['tj', 'uj', 'y(tj)', '|y(tj) - uj|']
    table = [[h*i, u[i], F(h*i), abs(F(h*i) - u[i])] for i in range(0, len(u))]
    return table


def func(y, t):
    return y - t**2 + 1


def Func(t):
    return (t+1)**2 - 0.5*sp.exp(t)


print Euler(0.5, func, 0.2, 0, 2)
print ExactValueTableEuler(0.5, func, 0.2, 0, 2, Func)


"""
Ejercicios 05-17-2017
"""


def T(f, tn, yn, h, r):
    res = f.subs([(y, yn), (t, tn)])
    dit = res
    diy = res
    for i in range(1, r-1):
        dit = sp.diff(dit, t, t)
        diy = sp.diff(diy, y, y)
        res += (1/math.factorial(i)) * (h**i) * (dit + diy)

    return res


def Taylor(y0, f, h, a, b, r):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h*T(f, tj, u[i], h, r))
        i += 1
        tj += h
    return u


def ExactValueTableTaylor(y0, f, h, a, b, r, F):
    u = Taylor(y0, f, h, a, b, r)
    row = ['tj', 'uj', 'y(tj)', '|y(tj) - uj|']
    table = [[h*i, u[i], F(h*i), abs(F(h*i) - u[i])] for i in range(0, len(u))]
    return table


def EulerMejorado(y0, f, h, a, b):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h*f(tj + h/2, u[i] + h/2*f(tj, u[i])))
        i += 1
        tj += h
    return u


def PuntoMedio(y0, f, h, a, b):
    u = []
    u.append(y0)
    i = 1
    u.append(Euler(y0, f, h, a, a+h))
    tj = a
    while tj + h < b:
        u.append(u[i] + 2*h*f(tj, u[i]))
        i += 1
        tj += h
    return u


def gunc(y, t):
    return y**2/(1 + t)


def Gunc(t):
    return -1/sp.log(t + 1)


print "\n\n Exercises 05-17-2017"


y0 = -1/math.log(2)

guncf = y**2/(1 + t)

print "Derivada respecto t: ", sp.diff(gunc(y, t), t)
print "Derivada respecto y: ", sp.diff(gunc(y, t), y)
print "Segunda derivada respecto t: ", sp.diff(gunc(y, t), t, t)
print "Segunda derivada respecto y: ", sp.diff(gunc(y, t), y, y)
print "\nTaylor de orden 2"
print Taylor(y0, gunc(y, t), 0.1, 1, 2, 2)
print "\nTaylor de orden 4\n"
print Taylor(y0, gunc(y, t), 0.1, 1, 2, 4)

print "\nErrores con Taylor de orden 2"
print ExactValueTableTaylor(y0, gunc(y, t), 0.1, 1, 2, 2, Gunc)
print "\nErrores con Taylor de orden 4"
print ExactValueTableTaylor(y0, gunc(y, t), 0.1, 1, 2, 4, Gunc)

print "Punto medio usando Euler", PuntoMedio(y0, gunc(y, t), 0.1, 1, 2)


""" -------------------------------------- """
""" Estas Funciones no están del todo bien """
""" -------------------------------------- """
"""
Exercises of 05-24-2017
9,12,13,15
"""

"""
Crank-Nikolson
"""


def K1CN(f, tj, uj):
    return f(tj, uj)


def K2CN(f, c2, h, tj, uj):
    return f(tj + c2*h, uj + c2*h*K1CN(f, tj, uj))


def CrankNikolson(y0, f, h, b1, b2, c2, a, b):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h*(b1*K1CN(f, tj, u[i]) + b2*K2CN(f, c2, h, tj, u[i])))
        i += 1
        tj += h
    return u


def EulerMejoradoCrackNikolson(y0, f, h, a, b):
    return CrankNikolson(y0, f, h, 0, 1, 1/2, a, b)


def Heun(y0, f, h, a, b):
    return CrankNikolson(y0, f, h, 1/2, 1/2, 1, a, b)


"""
Runge-Kutta orden 4
"""


def K1RK(f, tj, uj):
    return f(tj, uj)


def K2RK(f, h, tj, uj):
    return f(tj + h/2, uj + h/2*K1RK(f, tj, uj))


def K3RK(f, h, tj, uj):
    return f(tj + h/2, uj + h/2*K2RK(f, tj, uj))


def K3RK(f, h, tj, uj):
    return f(tj + h, uj + h*K3RK(f, tj, uj))


def RungeKutta(y0, f, h, a, b):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h/6*(K1RK(f, tj, u[i]) + K2RK(f, h, tj, u[i]) + K3RK(f, h, tj, u[i]) + K4RK(f, h, tj, u[i])))
        i += 1
        tj += h
    return u


"""
Adams-Bashforth 4 pasos
"""

"""
def AdamsBashforth(y0, f, h, a, b):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h/24*(55*fj - 59*fj_1 + 37*fj_2 + - 9*fj_3))
        i += 1
        tj += h
    return u
"""

"""
Adams-Moulton 4 pasos
"""

"""
def AdamsMoulton(y0, f, h, a, b):
    u = []
    u.append(y0)
    i = 0
    tj = a
    while tj + h < b:
        u.append(u[i] + h/720*(251*fj1 + 649*fj - 264*fj_1 + 106*fj_2 - 19*fj_3))
        i += 1
        tj += h
    return u
"""
