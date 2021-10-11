import math
from sympy import symbols, Eq, solve, sin, cos


def runFunction(index, variables):
    try:
        return eval(functions[index])
    except Exception:
        return "Error!"


def para1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * variables[2])
    return solve(eq1)[0]


def tri1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 0.5 * variables[1] * variables[2])
    return solve(eq1)[0]


def trap1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (variables[1] + variables[2]) * 0.5 * variables[3])
    return solve(eq1)[0]


def circ1(variables):
    for i in range(2):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (variables[1] ** 2) * math.pi)
    return math.fabs(solve(eq1)[0])


def cyl1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 2 * math.pi * variables[1] * variables[2])
    return solve(eq1)[0]


def circ2(variables):
    for i in range(2):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 2 * math.pi * variables[1])
    return solve(eq1)[0]


def cub1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * variables[2] * variables[3])
    return solve(eq1)[0]


def cyl2(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[2] * math.pi * variables[1] ** 2)
    return math.fabs(solve(eq1)[0])


def pris1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 0.5 * variables[1] * variables[2] * variables[3])
    return solve(eq1)[0]


def term1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] + (variables[2] - 1) * variables[3])
    return solve(eq1)[0]


def term2(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * (variables[2] ** (variables[3] - 1)))
    return solve(eq1)[0]


def sum1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 0.5 * variables[1] * (2 * variables[2] + (variables[1] - 1) * variables[3]))
    return solve(eq1)[0]


def sum2(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (variables[1] * (variables[2] ** variables[3] - 1))/(variables[2] - 1))
    return solve(eq1)[0]


def sum3(variables):
    if variables[2] != "" and math.fabs(variables[2]) >= 1:
        return "Invalid r value!"
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] / (1 - variables[2]))
    return solve(eq1)[0]


def int1(variables):
    for i in range(5):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * ((1 + (variables[2] * 0.01) / variables[3]) ** (variables[3] * variables[4])))
    return solve(eq1)[0]


def comb1(variables):
    return math.comb(variables[1], variables[2])


def perm1(variables):
    return math.perm(variables[1], variables[2])


def axi1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (-1 * variables[2])/(2 * variables[1]))
    return solve(eq1)[0]


def quad1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (-1 * variables[2] + (variables[2] ** 2 - (4 * variables[1] * variables[3])) ** 0.5)
             / (2 * variables[1]))
    if type(variables[0]) != int:
        eq2 = Eq(variables[0], (-1 * variables[2] - (variables[2] ** 2 - (4 * variables[1] * variables[3])) ** 0.5)
                 / (2 * variables[1]))
        return f"{solve(eq1)[0]}, {solve(eq2)[0]}"
    return solve(eq1)[0]


def disc1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[2] ** 2 - (4 * variables[1] * variables[3]))
    return solve(eq1)[0]


def pyr1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (1 / 3) * variables[1] * variables[2] * variables[3])
    return solve(eq1)[0]


def con1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (1 / 3) * math.pi * variables[1] ** 2 * variables[2])
    return solve(eq1)[0]


def sph1(variables):
    for i in range(2):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (4 / 3) * math.pi * variables[1] ** 3)
    return solve(eq1)[0]


def con2(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], math.pi * variables[1] * variables[2])
    return solve(eq1)[0]


def sph2(variables):
    for i in range(2):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 4 * math.pi * variables[1] ** 2)
    return solve(eq1)[0]


def sin1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0] / sin(variables[2]), variables[1] / sin(variables[3]))
    return solve(eq1)[0]


def cos1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[2] ** 2, variables[0] ** 2 + variables[1] ** 2 -
             2 * variables[0] * variables[1] * cos(variables[3]))
    return solve(eq1)[0]


def tri2(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 0.5 * variables[1] * variables[2] * sin(variables[3]))
    return solve(eq1)[0]


def arc1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * variables[2])
    return solve(eq1)[0]


def sec1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], 0.5 * variables[1] ** 2 * variables[2])
    return solve(eq1)[0]


def mag1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], (variables[1] ** 2 + variables[2] ** 2) ** 0.5)
    return solve(eq1)[0]


def dot1(variables):
    for i in range(5):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * variables[3] + variables[2] * variables[4])
    return solve(eq1)[0]


def ang1(variables):
    for i in range(4):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(cos(variables[0]), (variables[1] * variables[3] + variables[2] * variables[4]) /
             (((variables[1] ** 2 + variables[2] ** 2) ** 0.5) * ((variables[3] ** 2 + variables[4] ** 2) ** 0.5)))
    return solve(eq1)[0]


functions = ['para1(variables)', 'tri1(variables)', 'trap1(variables)', 'circ1(variables)', 'cyl1(variables)',
             'circ2(variables)', 'cub1(variables)', 'cyl2(variables)', 'pris1(variables)', 'term1(variables)',
             'term2(variables)', 'sum1(variables)', 'sum2(variables)', 'sum3(variables)', 'int1(variables)',
             'comb1(variables)', 'perm1(variables)', 'axi1(variables)', 'quad1(variables)', 'disc1(variables)',
             'pyr1(variables)', 'con1(variables)', 'sph1(variables)', 'con2(variables)', 'sph2(variables)',
             'sin1(variables)', 'cos1(variables)', 'tri2(variables)', 'arc1(variables)', 'sec1(variables)',
             'mag1(variables)', 'dot1(variables)', 'ang1(variables)']
