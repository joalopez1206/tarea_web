import pymysql
from utils.artesano import Artesano
from utils.hincha import Hincha
import filetype
import hashlib
from flask import url_for
from werkzeug.utils import secure_filename
import os

DB_NAME = "tarea2"
DB_USERNAME = "dbtarea2"
DB_PASSWORD = "dbtarea2"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

UPLOAD_FOLDER = 'static/uploads'

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

def check_deportes(deporte: str):
    conn = get_conn()
    cursor = conn.cursor()

    query = "SELECT EXISTS(SELECT * from deporte WHERE nombre=%s) AS res;"
    cursor.execute(query, (deporte))
    val, = cursor.fetchone()
    if val:
        return True
    return False

def insert_hincha(hincha: Hincha):
    conn = get_conn()
    cursor = conn.cursor()
    # Primero obtengamos la id de la region
    region_id_query = "SELECT id FROM region WHERE nombre = %s"
    region = hincha.region
    cursor.execute(region_id_query, (region))
   
    region_id, = cursor.fetchone()
    # Luegoo la id de la comuna
    comuna_id_query = "SELECT id FROM comuna WHERE region_id = %s AND nombre = %s"
    comuna = hincha.comuna
    cursor.execute(comuna_id_query, (region_id, comuna))
    comuna_id, = cursor.fetchone()

    # Insertamos las ids
    QUERY = "INSERT INTO hincha (comuna_id, modo_transporte, nombre, email, celular, comentarios) VALUES (%s,%s,%s,%s,%s,%s)"
    
    cursor.execute(QUERY, (comuna_id, hincha.modo_transporte, hincha.name, hincha.mail, hincha.numero, hincha.comentario))
    
    QUERY = "SELECT id FROM hincha ORDER BY id DESC LIMIT 1"
    cursor.execute(QUERY)
    hincha_id, = cursor.fetchone()

    for deporte in hincha.deportes:
        QUERY = "SELECT id from deporte WHERE nombre = %s" 
        cursor.execute(QUERY, (deporte,))
        tipo_deporte_id, = cursor.fetchone()
        
        QUERY = "INSERT INTO hincha_deporte (hincha_id, deporte_id) VALUES (%s,%s)"
        cursor.execute(QUERY, (hincha_id, tipo_deporte_id))

    conn.commit()
    print("Insercion OK")
    return True

def insert_artesano(artesano: Artesano, images):
    conn = get_conn()
    cursor = conn.cursor()
    # Primero obtengamos la id de la region
    region_id_query = "SELECT id FROM region WHERE nombre = %s"
    region = artesano.region
    cursor.execute(region_id_query, (region))
   
    region_id, = cursor.fetchone()
    # Luegoo la id de la comuna
    comuna_id_query = "SELECT id FROM comuna WHERE region_id = %s AND nombre = %s"
    comuna = artesano.comuna
    cursor.execute(comuna_id_query, (region_id, comuna))
    comuna_id, = cursor.fetchone()

    # Insertamos las ids
    QUERY = "INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s,%s,%s,%s,%s)"
    
    cursor.execute(QUERY, (comuna_id, artesano.comentario, artesano.name, artesano.mail, artesano.numero))
    
    QUERY = "SELECT id FROM artesano ORDER BY id DESC LIMIT 1"
    cursor.execute(QUERY)
    artesano_id, = cursor.fetchone()
    
    for arte in artesano.artesanias:
        QUERY = "SELECT id from tipo_artesania WHERE nombre = %s" 
        cursor.execute(QUERY, (arte,))
        tipo_art_id, = cursor.fetchone()
        
        QUERY = "INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s,%s)"
        cursor.execute(QUERY, (artesano_id, tipo_art_id))
    
    ## Ahora insertaremos las imagenes, codigo extraido del aux

    for image in images:
        _filename = hashlib.sha256(
            secure_filename(image.filename) # nombre del archivo
            .encode("utf-8") # encodear a bytes
            ).hexdigest()
        _extension = filetype.guess(image).extension
        
        img_filename = f"{_filename}.{_extension}"
        
         # 2. save img as a file
        ruta = os.path.join(UPLOAD_FOLDER, img_filename)
        image.save(ruta)

        # insertamos la imagen en la base de datos
        QUERY = "INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s, %s, %s)"
        cursor.execute(QUERY, (UPLOAD_FOLDER, img_filename, artesano_id))

    conn.commit()
    print("Insercion OK")
    return True


def get_artesanos(page_size=5, offset=0):
    data = []
    conn = get_conn()
    cursor = conn.cursor()
    QUERY = "SELECT artesano.id, comuna.nombre, descripcion_artesania, artesano.nombre, email, celular FROM artesano, comuna WHERE artesano.comuna_id=comuna.id ORDER BY id DESC LIMIT %s, %s"
    
    cursor.execute(QUERY, (offset,page_size))
    artesanos = cursor.fetchall()

    for artesano in artesanos:
        artesano_id, nombre_comuna, descripcion_artesania, nombre_artesano, email, numero = artesano
        QUERY = "SELECT TA.nombre FROM tipo_artesania TA, artesano_tipo AT WHERE AT.tipo_artesania_id=TA.id AND AT.artesano_id = %s"
        cursor.execute(QUERY, (artesano_id,))
        tipo_artesanias = list(cursor.fetchall())
        tipo_artesanias = [x[0] for x in tipo_artesanias]
        
        QUERY = "SELECT ruta_archivo, nombre_archivo FROM foto WHERE artesano_id=%s"
        cursor.execute(QUERY, (artesano_id,))
        imagenes = cursor.fetchall()
        imagenes = [f"uploads/{nombre}" for _,nombre in imagenes]
        imagenes = [url_for('static', filename=img_filename) for img_filename in imagenes]
        data.append({
            "artesano_id": artesano_id,
            "nombre_comuna": nombre_comuna,
            "descripcion_artesania": descripcion_artesania,
            "nombre" : nombre_artesano,
            "email": email,
            "numero": numero,
            "tipo_artesanias": tipo_artesanias,
            "imagenes": imagenes
        })
    return data

#necesito: region, comuna , tipo_artesanias, comentarios, nombre, mail, numero
def get_artesano_by_id(artesano_id):
    conn = get_conn()
    cursor = conn.cursor()
    
    QUERY = "SELECT comuna_id, comuna.nombre, descripcion_artesania, artesano.nombre, email, celular FROM artesano, comuna WHERE artesano.comuna_id=comuna.id AND artesano.id = %s" 
    cursor.execute(QUERY, (artesano_id,))
    comuna_id, comuna, comentario, nombre, mail, numero = cursor.fetchone()
    
    QUERY = "SELECT TA.nombre FROM tipo_artesania TA, artesano_tipo AT WHERE AT.tipo_artesania_id=TA.id AND AT.artesano_id = %s"
    cursor.execute(QUERY, (artesano_id,))
    tipo_artesanias = list(cursor.fetchall())
    tipo_artesanias = [x[0] for x in tipo_artesanias]

    QUERY = "SELECT region.nombre FROM region, comuna WHERE region.id = comuna.region_id AND comuna.id = %s"
    cursor.execute(QUERY, (comuna_id,))
    region_name, = cursor.fetchone()

    QUERY = "SELECT ruta_archivo, nombre_archivo FROM foto WHERE artesano_id=%s"
    cursor.execute(QUERY, (artesano_id,))
    imagenes = cursor.fetchall()
    imagenes = [f"uploads/{nombre}" for _,nombre in imagenes]
    imagenes = [url_for('static', filename=img_filename) for img_filename in imagenes]
    data = {
        "region":region_name,
        "comuna":comuna,
        "tipo_artesanias":tipo_artesanias,
        "descripcion_artesania":comentario,
        "nombre":nombre,
        "mail":mail,
        "numero":numero,
        "imagenes":imagenes
    }
    return data

def get_hinchas(page_size=5, offset=0):
    data = []
    conn = get_conn()
    cursor = conn.cursor()
    QUERY = "SELECT hincha.id, comuna.nombre, comentarios, hincha.nombre, email, celular, modo_transporte FROM hincha, comuna WHERE hincha.comuna_id=comuna.id ORDER BY id DESC LIMIT %s, %s"
    
    cursor.execute(QUERY, (offset,page_size))
    hinchas = cursor.fetchall()

    for hincha in hinchas:
        hincha_id, nombre_comuna, comentarios, nombre_hincha, email, numero, modo_transporte = hincha
        QUERY = """SELECT DP.nombre
        FROM deporte DP, hincha_deporte HP
        WHERE DP.id=HP.deporte_id AND HP.hincha_id = %s"""
        cursor.execute(QUERY, (hincha_id,))
        tipo_deportes = list(cursor.fetchall())
        tipo_deportes = [x[0] for x in tipo_deportes]
        
        data.append({
            "hincha_id": hincha_id,
            "nombre_comuna": nombre_comuna,
            "comentarios": comentarios,
            "nombre" : nombre_hincha,
            "email": email,
            "numero": numero,
            "tipo_transporte": modo_transporte,
            "tipo_deportes": tipo_deportes,
        })
    print(data)
    return data


def get_hincha_by_id(hincha_id):
    conn = get_conn()
    cursor = conn.cursor()
    
    QUERY = "SELECT comuna_id, comuna.nombre, comentarios, hincha.nombre, email, celular, modo_transporte FROM hincha, comuna WHERE hincha.comuna_id=comuna.id AND hincha.id = %s" 
    cursor.execute(QUERY, (hincha_id,))
    comuna_id, comuna, comentarios, nombre, mail, numero, modo_transporte = cursor.fetchone()
    
    QUERY = """SELECT DP.nombre
        FROM deporte DP, hincha_deporte HP
        WHERE DP.id=HP.deporte_id AND HP.hincha_id = %s"""
    cursor.execute(QUERY, (hincha_id,))
    tipo_deportes = list(cursor.fetchall())
    tipo_deportes = [x[0] for x in tipo_deportes]

    QUERY = "SELECT region.nombre FROM region, comuna WHERE region.id = comuna.region_id AND comuna.id = %s"
    cursor.execute(QUERY, (comuna_id,))
    region_name, = cursor.fetchone()

    data = {
        "region":region_name,
        "comuna":comuna,
        "tipo_deportes":tipo_deportes,
        "comentarios":comentarios,
        "nombre":nombre,
        "mail":mail,
        "numero":numero,
        "modo_transporte":modo_transporte
    }
    return data