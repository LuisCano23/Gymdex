from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager  
from app.routes import routes

db = SQLAlchemy()
# login_manager = LoginManager()  

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecreto123"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    db.init_app(app)
    # login_manager.init_app(app)  

    app.register_blueprint(routes)  

    return app
