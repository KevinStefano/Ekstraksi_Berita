#set FLASK_APP=flasktest.py
#flask run

from flask import Flask,render_template
from flask import request, redirect, url_for
from regex import mainProgram

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def about():
    if request.method =="POST":
        return render_template('form.html')
    else:
        return render_template('home.html')

@app.route("/form", methods = ["POST", "GET"])
def home():
    if request.method =="POST":
        foldr = request.form["folder"]
        key =request.form["keyword"]
        algo =request.form["algo"]
        hasil = mainProgram(foldr,key,algo)
        hasil.append("Berita diambil dari folder : " + foldr)
        return render_template('form.html', error= hasil)
    #     return redirect(url_for("haiho", usr = user))
    else:
        return render_template('form.html')

@app.route("/calculate")
def calculate():
    return 0

@app.route("/<usr>")
def haiho(usr):
    return render_template('form.html', error= usr)

if __name__ == '__main__':
    app.run(debug = True)