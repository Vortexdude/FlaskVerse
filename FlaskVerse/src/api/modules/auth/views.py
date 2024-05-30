from flask.views import MethodView
from . import blp
from .params import LoginParams

@blp.route("/login")
class LoginView(MethodView):
    @blp.arguments(LoginParams, location="json")
    def post(self, data):
        # print(data)
        return {"Status": "Done"}
