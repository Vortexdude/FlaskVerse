from .db.db_instance import db
from .api import api, spec_kwargs


def init_app(app):
    for ext in [db]:
        ext.init_app(app)
    api.init_app(app)
