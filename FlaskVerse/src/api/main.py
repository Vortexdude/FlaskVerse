import os
from FlaskVerse.src.extentions.flask import Flask
from FlaskVerse.src.extentions import init_app


CONFIG_MAPPING = {
    'development': 'config/development.toml',
    'production': 'config/production.toml',
    'testing': 'config/testing.toml'

}


def create_app(config_name='development'):
    app = Flask(__name__)
    config_type = os.environ.get("FLASK_ENV", config_name)
    app.config.from_toml(CONFIG_MAPPING[config_type])
    init_app(app)
    register_module(app)
    return app


def register_module(app):
    from FlaskVerse.src.api import modules
    modules.init_app(app)


app = create_app()

app.run(host="0.0.0.0", port=5000, debug=True)
