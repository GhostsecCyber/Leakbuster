from marshmallow import Schema, ValidationError, fields
from flask import abort


class UserSchema(Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)
    roles = fields.String(required=False)
    phone = fields.String(required=True)
    email = fields.Email(required=True)
    callback = fields.Url(required=True)
    site = fields.Url(required=True)
    company = fields.String(required=True)
    cdomain = fields.String(required=True)


class ValidationData:

    def __init__(self, json_data):
        try:
            schema = UserSchema()
            schema.load(json_data)

            if json_data['roles'] not in ['admin', 'user']:
                raise ValidationError('Invalid role provided')
            return
        except KeyError:
            return
        except ValidationError as err:
            abort(400, err.messages)
