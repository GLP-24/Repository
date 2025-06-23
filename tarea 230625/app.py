from flask import Flask, request, jsonify, render_template
from flask_restful import Api
from models import db
from user import UserF
from task import TaskF
import os

app = Flask(__name__)
api = Api(app)

# Configuración de SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar recursos
api.add_resource(UserF, 
                '/api/users',                         # GET (todos), POST (crear)
                '/api/users/<string:user_id>',        # GET, PUT, DELETE por ID
                '/api/users/dni/<string:dni>',        # GET por DNI
                endpoint='users')

api.add_resource(TaskF, 
                '/api/tasks',                         # GET (todos), POST (crear)
                '/api/tasks/<int:task_id>',          # GET, PUT, DELETE por ID
                '/api/tasks/user/<int:user_id>',     # GET tareas por usuario
                endpoint='tasks')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "<h1>POST hello world</h1>"
    else:
        resp1 = "hello world"
        resp2 = "<h2>hello world</h2>"
        resp3 = "<h3>hello world</h3>"
        resp4 = "<h4>hello world</h4>"
        resp5 = "<h5>hello world</h5>"
        resp6 = "<h6>hello world</h6>"
        name = 'Daniel'
        result = resp1 + resp2 + resp3 + resp4 + resp5 + resp6 + name
        return render_template("index.html", result=result, resp=resp1)


@app.route("/about/<int:id>", methods=["GET", "POST"])
def about(id):
    if request.method == "POST":
        return "<h1>POST hello world</h1>"
    else:
        datos = {"id": 1, "name": "Daniel", "age": 55}
        if id == datos["id"]:
            return jsonify(datos), 200
        else:
            return jsonify({"error": "No se encontraron datos"}), 204


@app.route("/user/<user_id>", methods=["GET"])
def personal_data(user_id):
    datos = UserF().get(user_id=user_id)
    if isinstance(datos, tuple):
        datos = datos[0]
        print("Datos obtenidos:", datos)
    print(datos)
    if datos:
        return render_template('personal_data.html', datos=datos)
    else:
        # If no data found, return an empty template or handle accordingly
        return render_template('personal_data.html', datos=None)


@app.route("/userdni/<dni>", methods=["GET"])
def personal_data_dni(dni):
    datos = UserF().get(dni=dni)
    if isinstance(datos, tuple):
        datos = datos[0]
        print("Datos obtenidos:", datos)
    print(datos)
    if datos:
        return render_template('personal_data.html', datos=datos)
    else:
        # If no data found, return an empty template or handle accordingly
        return render_template('personal_data.html', datos=None)

# Crear todas las tablas (reemplaza la función create_table())
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)