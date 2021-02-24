""" Main file """
from flgame.ext.config import init_app
from flask import Flask


def create_app() -> Flask:
    """Create a Flask app

    Returns:
        Flask: Instance of Flask
    """
    from tensorflow import keras

    # Get Instance of Flask
    app = Flask(__name__)

    # Load modules
    init_app(app)

    return app
