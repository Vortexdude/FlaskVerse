from importlib import import_module

ENABLED_MODULES = ["auth"]


def init_app(app):
    for module_name in ENABLED_MODULES:
        module = import_module(f"FlaskVerse.src.api.modules.{module_name}", "app")
        module.init_app(app)
