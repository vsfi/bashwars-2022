#!/usr/bin/env python
import json
import hashlib
import os


from flask import Flask, request

app = Flask(__name__)

# credentials
USER = 'bbalance'
PASSWORD = hashlib.md5(USER.encode('utf-8')).hexdigest()[::-1]
NEWBIE_PASSWORD = hashlib.md5((USER + '\n').encode('utf-8')).hexdigest()[::-1]

# errors
FAIL_MESSAGE = {"error": "Sorry, your princess is in another castle"}
UNAUTHORIZED_MESSAGE = {
    "error": "Invalid credentials. I'm calling the police."}
UA_ERROR_MESSAGE = {"error": "Invalid user-agent. Beware!."}
NEWBIE_ERROR = {"error": "Invalid credentials. I'm calling the police. Newline, captain? Huh."}

# load json data
JSON_DATA = {}
with open(os.path.dirname(__file__) + '/data.json') as json_file:
    JSON_DATA = json.load(json_file)


class InvalidUA(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class NoobError(Exception):
    pass


def checkUA(request_object):
    if 'curl' in request_object.headers.get('User-Agent'):
        raise InvalidUA


def getJSONResponse(obj, r_status=200):
    return app.response_class(
        response=json.dumps(obj),
        status=r_status,
        mimetype='application/json'
    )


def checkAuth(request_object):
    user_auth = request_object.authorization
    if not user_auth or not user_auth.username or not user_auth.password:
        raise InvalidCredentials
    if user_auth.username == USER and user_auth.password == NEWBIE_PASSWORD:
        raise NoobError
    if user_auth.username == USER and user_auth.password == PASSWORD:
        return True
    raise InvalidCredentials


@app.route('/')
def root():
    try:
        checkUA(request)
        checkAuth(request)
        return getJSONResponse(JSON_DATA, 200)
    except InvalidUA:
        return getJSONResponse(UA_ERROR_MESSAGE, 406)
    except InvalidCredentials:
        return getJSONResponse(UNAUTHORIZED_MESSAGE, 401)
    except NoobError:
        return getJSONResponse(NEWBIE_ERROR, 401)
    except Exception as e:
        return getJSONResponse(FAIL_MESSAGE, 400)
