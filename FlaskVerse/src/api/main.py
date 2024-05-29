import os

from FlaskVerse.src.extentions.flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from FlaskVerse.src.api.route.auth import blp as AuthBlueprint


CONFIG_MAPPING = {
    'development': 'config/development.toml',
    'production': 'production.toml',
    'testing': 'testing.toml'

}


def create_app(config_name='development'):
    app = Flask(__name__)
    config_type = os.environ.get("FLASK_ENV", config_name)
    app.config.from_toml(CONFIG_MAPPING[config_type])
    api = Api(app)
    register_blueprint(api)
    return app


def register_blueprint(api):
    api.register_blueprint(AuthBlueprint)


app = create_app()

app.run(host="0.0.0.0", port="5000")
