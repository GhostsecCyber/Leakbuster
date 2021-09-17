from functools import wraps
from flask import request


def validate_request(schema):
    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            schema(request.json)
            return func(*args, **kwargs)
        return wrap
    return wrapper
