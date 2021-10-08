import math
from sympy import symbols, Eq, solve


def runFunction(index, variables):
    return eval(functions[index])


def para1(variables):
    for i in range(3):
        if variables[i] == "":
            variables[i] = symbols('x')
    eq1 = Eq(variables[0], variables[1] * variables[2])
    return solve(eq1)[0]

def tri1(variables):
    pass

functions = ['para1(variables)', 'tri1(variables)', 'trap1(variables)', 'circ1(variables)', 'cyl1(variables)',
             'circ2(variables)', 'cub1(variables)', 'cyl2(variables)', 'pris1(variables)', 'poi1(variables)',
             'poi2(variables)', 'term1(variables)', 'term2(variables)', 'sum1(variables)', 'sum2(variables)',
             'sum3(variables)', 'int1(variables)', 'comb1(variables)', 'perm1(variables)', 'gra1(variables)',
             'axi1(variables)', 'quad1(variables)', 'disc1(variables)', 'poi3(variables)', 'poi4(variables)',
             'pyr1(variables)', 'con1(variables)', 'sph1(variables)', 'con2(variables)', 'sph2(variables)',
             'sin1(variables)', 'cos1(variables)', 'tri2(variables)', 'arc1(variables)', 'sec1(variables)',
             'mag1(variables)', 'dot1(variables)', 'ang1(variables)']

