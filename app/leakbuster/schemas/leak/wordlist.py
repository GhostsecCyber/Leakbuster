from marshmallow import Schema, ValidationError, fields
from flask import abort


class WordlistSchema(Schema):

    password = fields.String(required=True)


class ValidationData:

    def __init__(self, json_data):
        try:
            schema = WordlistSchema()
            schema.load(json_data)
            return
        except ValidationError as err:
            abort(400, err.messages)
