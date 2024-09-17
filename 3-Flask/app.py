from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)