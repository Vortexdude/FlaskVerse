from marshmallow import Schema, fields


class UserTokenSchema(Schema):
    access_token = fields.Str(description="access_token for the user")
    refresh_token = fields.Str(description="access_token for the user")


class UserDataSchema(Schema):
    tokens = fields.Nested(UserTokenSchema, description="Tokens")
