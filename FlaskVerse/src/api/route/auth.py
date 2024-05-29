from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint("Auth", __name__, description="Auth endpoint.")


@blp.route("/login")
class AuthClass(MethodView):

    def get(self):
        return {"Status": "Done"}
