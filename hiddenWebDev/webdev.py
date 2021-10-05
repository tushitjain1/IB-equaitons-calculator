from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    val = 0
    pics = ['para1', 'tri1', 'trap1', 'circ1', 'cyl1', 'circ2', 'cub1', 'cyl2', 'pris1', 'poi1', 'poi2', 'term1',
            'term2', 'sum1', 'sum2', 'sum3', 'int1', 'comb1', 'perm1', 'gra1', 'axi1', 'quad1', 'disc1', 'poi3',
            'poi4', 'pyr1', 'con1', 'sph1', 'con2', 'sph2', 'sin1', 'cos1', 'tri1', 'arc1', 'sec1', 'mag1',
            'dot1', 'ang1']
    if request.method == 'GET':
        val = 0
    if request.method == 'POST':
        for k in request.form.keys():
            val = pics.index(k) + 1
    return render_template("home.html", val=val)


if __name__ == '__main__':
    app.run(debug=True)
