from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/agregar_artesano",methods=["GET", "POST"])
def agregar_artesano():
    if request.method == "GET":
        return render_template("agregar-artesano.html")
    elif request.method == "POST":
        return "<p>NO PASA NA</p>"
    

@app.route("/agregar_hincha",methods=["GET", "POST"])
def agregar_hincha():
    if request.method == "GET":
        return render_template("agregar-hincha.html")
    elif request.method == "POST":
        return "<p>NO PASA NA</p>"

@app.route("/ver_artesanos",methods=["GET", "POST"])
def ver_artesanos():
    if request.method == "GET":
        return render_template("ver-artesanos.html")
    elif request.method == "POST":
        return "<p>NO PASA NA</p>"

@app.route("/ver_hinchas",methods=["GET", "POST"])
def ver_hinchas():
    if request.method == "GET":
        return render_template("ver-hinchas.html")
    elif request.method == "POST":
        return "<p>NO PASA NA</p>"

if __name__ == "__main__":
    app.run(debug=True)