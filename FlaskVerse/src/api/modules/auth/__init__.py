from FlaskVerse.src.extentions import api
from flask_smorest import Blueprint


blp = Blueprint("Auth", __name__, description="Auth endpoint.")


def init_app(app):
    from . import views
    api.register_blueprint(blp=blp)
