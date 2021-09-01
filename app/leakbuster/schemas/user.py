from marshmallow import Schema, ValidationError, fields, validate
from flask import abort


class UserSchema(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)
    roles = fields.String(validate=validate.OneOf(['admin', 'user']))
    phone = fields.String(required=True)
    email = fields.Email(required=True)
    site = fields.Url(required=True)
    company = fields.String(required=True)
    cdomain = fields.String(required=True)


class ValidationData:

    def __init__(self, json_data):
        try:
            schema = UserSchema()
            schema.load(json_data)

            return
        except KeyError:
            return
        except ValidationError as err:
            abort(400, err.messages)
