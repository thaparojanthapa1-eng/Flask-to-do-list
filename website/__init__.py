from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

Db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="Hello World"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{DB_NAME}"
    Db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    return app

def create_database(app):
    if not path.exists("website/"+DB_NAME):
        with app.app_context():
            Db.create_all()
        print("Created database!")