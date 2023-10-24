# Tarea 2
> autor: joalopez1206

Esta es la entrega de la tarea 2. 
Es un prototipo de pagina para los juegos paramericanos 2023 santiago con una base de datos

Dentro de cada carpeta estan todos los recursos que se usan
- __utils__ tiene utilidades para la app de flask (validaciones)
- __templates__ tiene los templates de html
- __static__ tiene los recursos estaticos usados (js, img, css)

Notar que la conexion a la base de datos es usando las siguientes variables:

```py
DB_NAME = "tarea2"
DB_USERNAME = "dbtarea2"
DB_PASSWORD = "dbtarea2"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"
```
## Como ejecutar

Para ejecutar esta tarea, primero hay que instalar los requierments con pip
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

crear una base de datos con mysql.

y por ultimo ejecutar

```bash
python3 app.py
```

## Observaciones del codigo

Las imagenes de guardan en la carpeta static! tambien lo que falta en el codigo es poder encoger las imagenes que se suben, para que se vean mejor en "ver-artesanos".

Por el momento solo se han subido imagenes de baja calidad!
