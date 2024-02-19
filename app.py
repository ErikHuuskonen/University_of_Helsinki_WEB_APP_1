from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import getenv


db = SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder='appi/templates',static_folder='appi/static')
    app.secret_key = getenv('SECRET_KEY')

    #For local
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

    #For deployment
    #app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("://", "ql://", 1)

    db.init_app(app)

    with app.app_context():
        import appi.routes

    return app



