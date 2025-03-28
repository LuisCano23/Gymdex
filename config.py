import os

class Config:
    SECRET_KEY = "supersecreto123"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"  # Base de datos SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva warnings innecesarios