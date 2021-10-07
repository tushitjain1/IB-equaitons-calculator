from flask import Flask, render_template,request
import math
app = Flask(__name__)
val = 0


@app.route('/', methods=['POST', 'GET'])
def home():
    global val
    calcText = ""
    pics = ['icon', 'para1', 'tri1', 'trap1', 'circ1', 'cyl1', 'circ2', 'cub1', 'cyl2', 'pris1', 'poi1', 'poi2',
            'term1', 'term2', 'sum1', 'sum2', 'sum3', 'int1', 'comb1', 'perm1', 'gra1', 'axi1', 'quad1', 'disc1',
            'poi3', 'poi4', 'pyr1', 'con1', 'sph1', 'con2', 'sph2', 'sin1', 'cos1', 'tri1', 'arc1', 'sec1', 'mag1',
            'dot1', 'ang1']
    if request.method == 'POST':
        for k in request.form.keys():
            if k in pics:
                val = pics.index(k)
            else:
                calcText = calculator(request.form[k])
    return render_template("home.html", val=val, answer=calcText)


def calculator(calcText):
    symbs = ["+", "-", "/", "*", "π", "^", "×"]
    pyInput = ""
    for i in range(len(calcText)):
        if calcText[i] == symbs[4]:
            pyInput += f"({math.pi})"
        elif calcText[i] == symbs[5]:
            pyInput += "**"
        elif calcText[i] == symbs[6]:
            pyInput += "*"
        else:
            pyInput += calcText[i]
    i = 1
    while i < len(pyInput) - 1:
        if pyInput[i] == "(" and pyInput[i-1] not in symbs:
            pyInput = pyInput[0:i] + "*" + pyInput[i:]
        if pyInput[i] == ")" and pyInput[i+1] not in symbs:
            pyInput = pyInput[0:i+1] + "*" + pyInput[i+1:]
        i += 1
    try:
        answer = eval(pyInput)
    except SyntaxError:
        return "Syntax Error!"
    except ZeroDivisionError:
        return "Zero Division Error!"
    return answer


if __name__ == '__main__':
    app.run(debug=True)
