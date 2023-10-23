import pymysql
from utils.artesano import Artesano

DB_NAME = "tarea2"
DB_USERNAME = "dbtarea2"
DB_PASSWORD = "dbtarea2"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

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

def insert_artesano(artesano: Artesano):
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
        print(tipo_artesanias)
        data.append({
            "artesano_id": artesano_id,
            "nombre_comuna": nombre_comuna,
            "descripcion_artesania": descripcion_artesania,
            "nombre" : nombre_artesano,
            "email": email,
            "numero": numero,
            "tipo_artesanias": tipo_artesanias
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

    data = {
        "region":region_name,
        "comuna":comuna,
        "tipo_artesanias":tipo_artesanias,
        "descripcion_artesania":comentario,
        "nombre":nombre,
        "mail":mail,
        "numero":numero
    }
    return data