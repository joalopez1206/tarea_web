# Tarea 3

> autor: joalopez1206

Esta es la entrega de la tarea 3. 
Es un prototipo de pagina para los juegos paramericanos 2023 santiago con una base de datos

Dentro de cada carpeta estan todos los recursos que se usan
- __utils__ tiene utilidades para la app de flask (validaciones)
- __templates__ tiene los templates de html
- __static__ tiene los recursos estaticos usados (js, img, css)
- __database__ tiene las funciones de mysql para interactuar con la base de datos

Notar que la conexion a la base de datos es usando las siguientes variables (no cambie lo de tarea2 por comodidad):

__IMPORTANTE__ : __Si es que no funciona logearse a la base de datos, intente dejando en una terminal la base de datos prendida y probar la aplicacion denuevo.__

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

## Estado y Observaciones del codigo

Incluyendo lo de la tarea 2, ahora se puede registrar y ver hinchas.

Tambien se añadio la nueva funcionalidad de graficos, los cuales son los archivos stats.`(html|js|css)` los cuales son para
realizar los graficas, los cuales son hechos por la libreria Highcharts y usando AJAX con la api `fetch` para cargar los datos.
