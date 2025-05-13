from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, login_user, logout_user, current_user
from app import db
from app.models import User, Publicacion
from app.forms import RegistrationForm, LoginForm, PublicacionForm
import json
import os

bp = Blueprint("routes", __name__)

@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists. Please choose a different one.", "danger")
            return redirect(url_for("main.login"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("routes.login"))
    return render_template("security/register.html", form=form)

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Form submitted")
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("routes.features"))
        else:
            flash("Invalid email or password. Please try again.", "danger")

    return render_template("security/login.html", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("routes.index"))

@bp.route("/features")
@login_required
def features():
    return render_template("features.html")

@bp.route("/compare")
def compare():
    json_path = os.path.join(current_app.root_path, 'static', 'gyms.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        gyms = json.load(file)
        
    return render_template("compare.html", gyms=gyms)

@bp.route("/simulation")
def simulation():
    return render_template("simulation.html")

@bp.route("/shop")
def shop():
    json_path = os.path.join(current_app.root_path, 'static', 'productos.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        productos = json.load(file)
    return render_template("shop.html", productos=productos)

@bp.route("/contacts", methods=["GET", "POST"])
@login_required
def contacts():
    form = PublicacionForm()
    if form.validate_on_submit():
        new_publicacion = Publicacion(
            profesion=form.profesion.data,
            contenido=form.contenido.data,
            telefono=form.telefono.data,
            email_contacto=form.email_contacto.data,
            autor_id=current_user.id
        )
        db.session.add(new_publicacion)
        db.session.commit()
        return redirect(url_for("routes.contacts")) 

    publicaciones = Publicacion.query.order_by(Publicacion.fecha_publicacion.desc()).all()
    return render_template("contacts.html", form=form, publicaciones=publicaciones)
