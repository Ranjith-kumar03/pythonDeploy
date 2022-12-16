from flask import Flask

def create_app(testconfig = None):
    app = Flask(__name__, instance_relative_config = True)

    if testconfig is None:

        app.config.from_mapping(

        )
    else:

        app.config.from_mapping(testconfig)

    return app
