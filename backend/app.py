from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../frontend')

import mysql.connector

mydb = None

try:
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,  
        user="root",
        password="xxxxxx",
        database="recipes_db"
    )
    print("¡Conexión exitosa a la base de datos!")
except mysql.connector.Error as err:
    if err.errno == 1045:
        print("Error de autenticación: Usuario o contraseña incorrectos.")
    elif err.errno == 1049:
        print("Error: La base de datos 'recipes_db' no existe.")
    else:
        print(f"Error al conectar a la base de datos: {err}")

if mydb is not None and mydb.is_connected():
    mycursor = mydb.cursor()


@app.route('/')
def index():
    return send_from_directory('../frontend/html', 'index.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../frontend/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('../frontend/js', path)

if __name__ == '__main__':
    app.run(debug=True)

from app import db
db.create_all()
