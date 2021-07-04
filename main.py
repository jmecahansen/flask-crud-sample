# flask-crud-sample
# pequeña aplicación con Flask para hacer operaciones CRUD (Crear, Leer, Actualizar y Borrar)

# importamos las librerías necesarias
from datetime import datetime
from flask import Flask, render_template, request
from src import db

# inicializamos la aplicación
app = Flask(__name__, template_folder="tpl")

# inicializamos la base de datos
db = db.DatabaseClass()


# ruta: página de inicio
@app.route("/")
def list_users():
    return render_template("main.html", data={
        "users": db.get_users()
    })


# ruta: AJAX (usuarios)
@app.route("/ajax/users", methods=["POST"])
def manage_user_requests():
    form = request.form.to_dict()
    response = {
        "success": False
    }

    if "function" in form.keys():
        if form["function"] == "delete_user":
            if "user_id" in form.keys():
                if db.delete_user(form["user_id"]):
                    response = {
                        "success": True
                    }
        elif form["function"] == "delete_user_location":
            if "user_id" in form.keys():
                if "location_id" in form.keys():
                    if db.delete_user_location(form["location_id"]):
                        response = {
                            "success": True
                        }
        elif form["function"] == "delete_user_record":
            if "user_id" in form.keys():
                if "record_id" in form.keys():
                    if db.delete_user_record(form["record_id"]):
                        response = {
                            "success": True
                        }

    return response


# ruta: perfil de usuario
@app.route("/users/<int:user_id>/", methods=["GET", "POST"])
def user_details(user_id):
    return render_template("users/profile.html", data={
        "user": db.get_user(user_id),
        "locations": db.get_user_locations(user_id),
        "records": db.get_user_records(user_id)
    })


# ruta: editar usuario
@app.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    form = request.form.to_dict()

    if len(form) > 0:
        db.update_user(user_id, form)

    return render_template("users/edit.html", data=db.get_user(user_id))


# ruta: editar ubicación de usuario
@app.route("/users/<int:user_id>/locations/<int:location_id>/edit", methods=["GET", "POST"])
def edit_user_location(user_id, location_id):
    form = request.form.to_dict()

    if len(form) > 0:
        db.update_user_location(location_id, form)

    return render_template("users/locations/edit.html", data={
        "user": db.get_user(user_id),
        "location": db.get_user_location(user_id, location_id)
    })


# ruta: editar registro de usuario
@app.route("/users/<int:user_id>/records/<int:record_id>/edit", methods=["GET", "POST"])
def edit_user_record(user_id, record_id):
    form = request.form.to_dict()

    if len(form) > 0:
        db.update_user_record(record_id, form)

    return render_template("users/records/edit.html", data={
        "user": db.get_user(user_id),
        "record": db.get_user_record(user_id, record_id)
    })


# ruta: nuevo usuario
@app.route("/users/new", methods=["GET", "POST"])
def new_user():
    form = request.form.to_dict()

    if len(form) > 0:
        db.insert_user(list(form.values()))

    return render_template("users/new.html")


# ruta: nueva ubicación de usuario
@app.route("/users/<int:user_id>/locations/new", methods=["GET", "POST"])
def new_user_location(user_id):
    form = request.form.to_dict()

    if len(form) > 0:
        db.insert_user_location(user_id, list(form.values()))

    return render_template("users/locations/new.html", data={
        "user": db.get_user(user_id),
        "current_year": datetime.now().strftime("%Y")
    })


# ruta: nuevo registro de usuario
@app.route("/users/<int:user_id>/records/new", methods=["GET", "POST"])
def new_user_record(user_id):
    form = request.form.to_dict()

    if len(form) > 0:
        db.insert_user_record(user_id, list(form.values()))

    return render_template("users/records/new.html", data={
        "user": db.get_user(user_id),
        "current_year": datetime.now().strftime("%Y")
    })
