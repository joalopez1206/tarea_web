from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
from utils.validations import validate_entry_artesano#, validate_files_artesano
from database import db
from utils.artesano import Artesano
app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/agregar_artesano",methods=["GET", "POST"])
def agregar_artesano():
    error = None
    if request.method == "GET":
        return render_template("agregar-artesano.html", error=error)
    elif request.method == "POST":
        data = request.form
        artesania_values = data.getlist('artesania[]')
        nombre = data["nombre"]
        email = data["myemail"]
        number = data["mynumber"]
        comentarios = data["comentarios"]
        region = data["region"]
        comuna = data["comuna"]

        entry_artesano = Artesano(name=nombre, mail=email, numero=number,
                                   comentario=comentarios, region=region,
                                   comuna=comuna, artesanias=artesania_values)
        print(data["mynumber"], type(number))
        #files_artesano = request.files
        if validate_entry_artesano(entry_artesano): #and validate_files_artesano():
            if db.insert_artesano(entry_artesano):
                print("Todo OK")
                return redirect(url_for("agregar_artesano", error=error))
            error = "Error insertando a base de datos, verifique que cumpla!"
        else:
            error = "Error en la validacion de los datos. Verifique que cumplen los requisitos"
        return redirect(url_for("agregar_artesano", error=error))
    

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