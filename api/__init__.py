from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db: SQLAlchemy = SQLAlchemy()

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    from .views import main
    app.register_blueprint(main)
    CORS(app)
    return app
