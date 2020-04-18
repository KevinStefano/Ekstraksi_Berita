#set FLASK_APP=flasktest.py
#flask run

from flask import Flask,render_template
from flask import request, redirect, url_for
from regex import mainProgram

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def about():
    if request.method =="POST":
        return  redirect(url_for('form'))
    else:
        return render_template('home.html')

@app.route("/homes", methods = ["POST","GET"])
def homes():
    if request.method =="POST":
        return  redirect(url_for('form'))
    else:
        return render_template('home.html')

@app.route("/form", methods = ["POST", "GET"])
def form():
    if request.method =="POST":
        foldr = request.form["folder"]
        key =request.form["keyword"]
        algo =request.form["algo"]
        if foldr!='':
            hasil = mainProgram(foldr,key,algo)
            return render_template('form.html', error= hasil)
        else: 
            return render_template('form.html')
        
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug = True)
