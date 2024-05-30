from marshmallow import Schema, fields


class LoginParams(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
