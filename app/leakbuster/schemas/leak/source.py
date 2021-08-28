from marshmallow import Schema, ValidationError, fields
from flask import abort


class SourceSchema(Schema):
    url = fields.Url(required=True)
    date = fields.String(required=True)
    description = fields.String(required=True)
    author = fields.String(required=True)


class ValidationData:

    def __init__(self, json_data):
        try:
            schema = SourceSchema()
            schema.load(json_data)

            return
        except ValidationError as err:
            abort(400, err.messages)
