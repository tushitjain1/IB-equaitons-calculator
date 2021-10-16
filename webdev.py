import sys, os
sys.stdout = open(os.devnull, "w")
temp = os.getenv("TEMP")
sys.stderr = open(os.path.join(temp if temp is not None else "/tmp", "stderr-"+os.path.basename(sys.argv[0])), "w")
from flask import Flask, render_template,request
import webbrowser
import math
from functions import runFunction
app = Flask(__name__)
val = 0


@app.route('/', methods=['POST', 'GET'])
def home():
    global val
    calcText = ""
    answer = ""
    variables = dict()
    pics = ['icon', 'para1', 'tri1', 'trap1', 'circ1', 'cyl1', 'circ2', 'cub1', 'cyl2', 'pris1',
            'term1', 'term2', 'sum1', 'sum2', 'sum3', 'int1', 'comb1', 'perm1', 'axi1', 'quad1', 'disc1',
            'pyr1', 'con1', 'sph1', 'con2', 'sph2', 'sin1', 'cos1', 'tri2', 'arc1', 'sec1', 'mag1',
            'dot1', 'ang1']
    if request.method == 'POST':
        for k in request.form.keys():
            if k in pics:
                val = pics.index(k)
            else:
                if k == "calc-text":
                    calcText = calculator(request.form[k])
                else:
                    variables[k] = calculator(request.form[k])
        if val > 0 and len(variables) > 0:
            count = 0
            vals = []
            for v in variables:
                if variables[v] == "":
                    count += 1
                vals.append(variables[v])
            if count > 1:
                answer = "Multiple Unknowns Error!"
            elif count == 0:
                answer = "No Unknowns Error!"
            else:
                answer = str(runFunction(val - 1, vals))
    return render_template("home.html", val=val, calc=calcText, answer=answer)


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
    if pyInput == "":
        return pyInput
    try:
        answer = eval(pyInput)
    except SyntaxError:
        return "Syntax Error!"
    except ZeroDivisionError:
        return "Zero Division Error!"
    return answer

if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

    app.run(host="127.0.0.1", port=5000)
