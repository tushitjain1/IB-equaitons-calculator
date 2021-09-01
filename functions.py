import math
from sympy import symbols, Eq, solve


def areaParallelogram(vars):
    for i in range(3):
        if vars[i] is None:
            vars[i] = symbols('x')
    eq1 = Eq(vars[0]*vars[1], vars[2])
    return solve(eq1)


a = 10
b = 20
h = None
ok = areaParallelogram([b, h, a])
print(ok)
