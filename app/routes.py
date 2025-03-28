from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/register")
def register():
    return render_template("security/register.html")

@routes.route("/login")
def login():
    return render_template("security/login.html")
