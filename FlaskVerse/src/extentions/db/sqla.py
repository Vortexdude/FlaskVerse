from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy


class SQLAlchemy(BaseSQLAlchemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DuplicateEntry(Exception):
    """Duplicate type"""
    pass


class CharsTooLong(Exception):
    """Invalid characters length"""
    pass
