from flask_api import FlaskAPI


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object('config.py')

