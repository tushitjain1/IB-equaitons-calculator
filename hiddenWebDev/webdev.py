from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def home():
    val = 0
    pics = ['para1','tri1']
    if request.method == 'GET':
        val = 0
    if request.method == 'POST':
        if request.form['para1']:
            val = 1
        print('works')
    return render_template("home.html", val = val)

if __name__ == '__main__':
    app.run(debug=True)
