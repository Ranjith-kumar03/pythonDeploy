from flask import Flask
from src.database.database import db , User, Product
from src.blueprint_controllers.User import user
# from src.blueprint_controllers.Product import product
import os

def create_app(testconfig = None):
    app = Flask(__name__, instance_relative_config = True)

    if testconfig is None:

        app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI'),

        )
    else:

        app.config.from_mapping(testconfig)

    

    db.app = app
    db.init_app(app)
    @app.before_first_request
    def create_table():
        db.create_all()

    app.register_blueprint(user)
    # app.register_blueprint(Product)

    return app
