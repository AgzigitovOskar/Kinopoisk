from functools import wraps

import jwt
from constants import SECRET, ALGO
from flask import request, abort


def auth_required(func):
    """
        проверка авторизации пользователя
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']

        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, SECRET, algorithms=[ALGO])

        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)

        return func(*args, **kwargs)
    return wrapper
