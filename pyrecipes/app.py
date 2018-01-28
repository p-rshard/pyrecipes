"""Main Flask module"""

from flask import Flask
from pyrecipes import api, errors
from pyrecipes.configuration import Config
from pyrecipes.extensions import db


def create_app(config=Config):
    """Flask application factory
    :param config: The configuration object
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """Register Flask extensions"""
    db.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints"""
    app.register_blueprint(api.blueprint)
    app.register_blueprint(errors.blueprint)
