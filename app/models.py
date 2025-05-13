from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class Publicacion(db.Model):
    __tablename__ = "publicaciones"
    
    id = db.Column(db.Integer, primary_key=True)
    profesion = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.String(300), nullable=False) 
    telefono = db.Column(db.String(20), nullable=False)
    email_contacto = db.Column(db.String(150), nullable=False)
    fecha_publicacion = db.Column(db.DateTime, default=datetime.utcnow)

    autor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    autor = db.relationship('User', backref=db.backref('publicaciones', lazy=True))