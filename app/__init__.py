import os

from flask import Flask
from . import receipts, errors
from app.errors import *
from jsonschema import exceptions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    app.register_blueprint(receipts.bp)
    app.register_error_handler(exceptions.ValidationError, handle_request_validation_error)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(500, handle_500)

    return app