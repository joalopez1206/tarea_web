from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
from utils.validations import validate_entry_artesano, validate_files_artesano, validate_entry_hincha
from database import db
from utils.artesano import Artesano
from utils.hincha import Hincha

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
ALL_GOOD = "Se ha registrado exitosamente!"

@app.route("/")
def menu():
    error = request.args.get('error', None)
    return render_template("index.html", error=error)

@app.route("/agregar_artesano",methods=["GET", "POST"])
def agregar_artesano():
    error = request.args.get('error', None)
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

        images = request.files.getlist('files[]')
        
        entry_artesano = Artesano(name=nombre, mail=email, numero=number,
                                   comentario=comentarios, region=region,
                                   comuna=comuna, artesanias=artesania_values)
        print(images)
        if validate_entry_artesano(entry_artesano) and validate_files_artesano(images):
            if db.insert_artesano(entry_artesano, images):
                print("Todo OK, artesano registrado!")
                error = ALL_GOOD
                return redirect(url_for("menu", error=error))
            error = "Error insertando a base de datos, verifique que cumpla!"
        else:
            error = "Error en la validacion de los datos. Verifique que cumplen los requisitos"
        return render_template("agregar-artesano.html", error=error)
    

@app.route("/agregar_hincha",methods=["GET", "POST"])
def agregar_hincha():
    error = request.args.get('error', None)
    if request.method == "GET":
        return render_template("agregar-hincha.html", error=error)
    elif request.method == "POST":
        data = request.form
        deportes_values = data.getlist('deportes[]')
        nombre = data["nombre"]
        email = data["myemail"]
        number = data["mynumber"]
        comentarios = data["comentarios"]
        region = data["region"]
        comuna = data["comuna"]
        transportes = data["transporte[]"]

        entry_hincha = Hincha(nombre,email,number,region,comuna,deportes_values,comentarios, transportes)

        print(data)
        if validate_entry_hincha(entry_hincha):
            if db.insert_hincha(entry_hincha):
                error = ALL_GOOD
                return redirect(url_for("menu", error=error))
            error = "Error insertado en la base de datos"
        else:
            error = "Error en la validacion de los datos. Verifique que cumplen los requisitos"
        return render_template("agregar-hincha.html", error = error)

@app.route("/ver_artesanos/<int:offset>",methods=["GET"])
def ver_artesanos(offset):
    if request.method == "GET":
        data = db.get_artesanos(offset=offset)
        return render_template("ver-artesanos.html", artesanos=data, offset=offset)
    
@app.route("/informacion_artesanos/<int:artesano_id>", methods=["GET"])
def informacion_artesanos(artesano_id):
    artesano = db.get_artesano_by_id(artesano_id)
    return render_template("informacion-artesanos.html",artesano=artesano)

@app.route("/informacion_hinchas/<int:hincha_id>", methods=["GET"])
def informacion_hinchas(hincha_id):
    artesano = db.get_hincha_by_id(hincha_id)
    return render_template("informacion-hincha.html",hincha=artesano)


@app.route("/ver_hinchas/<int:offset>",methods=["GET"])
def ver_hinchas(offset):
    if request.method == "GET":
        data = db.get_hinchas(offset=offset)
        return render_template("ver-hinchas.html", hinchas=data, offset=offset)

@app.route("/get_hinchas_por_deporte", methods=["GET"])
@cross_origin(origin="*", supports_credentials=True)
def get_hinchas_por_deporte():
    data=db.get_number_of_hinchas_grouped_by_deporte()
    return jsonify({"status" :"ok", "data":data})

@app.route("/get_artesanos_por_artesania", methods=["GET"])
@cross_origin(origin="*", supports_credentials=True)
def get_artesanos_por_artesania():
    data=db.get_artesanos_grouped_by_artesania()
    return jsonify({"status" :"ok", "data":data})

@app.route("/stats", methods = ["GET"])
def stats():
    return render_template("stats.html")

if __name__ == "__main__":
    app.run(debug=True)