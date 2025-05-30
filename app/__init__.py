from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()  

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)  
    login_manager.login_view = 'login'  

    with app.app_context():
        from . import models

        @login_manager.user_loader
        def load_user(user_id):
            from .models import User
            return User.query.get(int(user_id))

    from .routes import bp
    app.register_blueprint(bp)

    return app