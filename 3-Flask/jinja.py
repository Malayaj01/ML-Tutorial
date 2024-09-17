from flask import Flask, render_template, request, redirect, url_for
'''
    It creates an instance of flask class
    which will be your  WSGI(Web server gateway interface)
'''

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to MalluBess   KI pathshala"

@app.route("/index")
def index():
    return "Welcome to index"

@app.route("/about")
def about():
    return render_template('index.html')

# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello{name}!'
#     return render_template('form.html')

# varible Rule 
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res ="FAIL"

    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res ="FAIL"

    exp ={'score':score, "res":res}

    return render_template('result.html',results=exp)


## if confition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)


@app.route('/submit',methods = ['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4

    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=total_score))


if __name__ == "__main__":
    app.run(debug=True)