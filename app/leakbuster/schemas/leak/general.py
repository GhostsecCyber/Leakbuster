from marshmallow import Schema, ValidationError, fields
from flask import abort


class GeneralSchema(Schema):
    url = fields.Url(required=True)
    leak_id = fields.String(required=True)


class ValidationData:

    def __init__(self, json_data):
        try:
            schema = GeneralSchema()
            schema.load(json_data)
            return
        except ValidationError as err:
            abort(400, err.messages)
