#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

FLAG = "DverMneZapiliBistroDveerZapili\n"
UA_ERROR_MESSAGE = "Well, it's not Woopsen UA\n"
SECOND_UA_ERROR_MESSAGE = "Well, it's not Poopsen UA\n"
NOT_BIBA_BOBA = "Mah boy, it's not Woopsen/Poopsen UA and is not Bugulma!!\n"
BUGULMA = 'Yes, it is Bugulma\n'


class InvalidUA(Exception):
    pass


class UAnotExist(Exception):
    pass


class NotBibaBoba(Exception):
    pass


class Bugulma(Exception):
    pass


def isCurlUA(request_object):
    if 'Bugulma' in request_object.headers.get('User-Agent', ''):
        raise Bugulma
    if 'Poopsen' in request_object.headers.get('User-Agent', ''):
        return True
    elif 'Woopsen' in request_object.headers.get('User-Agent', ''):
        return False
    else:
        raise NotBibaBoba


def checkUA(request_object, needUA):
    if needUA and isCurlUA(request_object):
        raise InvalidUA
    if not needUA and not isCurlUA(request_object):
        raise UAnotExist


def answer(message, code):
    return app.response_class(
        response=message,
        status=code
    )


@app.route('/flag/<int:part>')
def return_flag_part(part):
    try:
        if part % 2 == 0:
            checkUA(request, needUA=True)
            return answer(FLAG[part], 200)
        else:
            checkUA(request, needUA=False)
            return answer(FLAG[part], 200)
    except InvalidUA:
        return answer(UA_ERROR_MESSAGE, 406)
    except UAnotExist:
        return answer(SECOND_UA_ERROR_MESSAGE, 406)
    except NotBibaBoba:
        return answer(NOT_BIBA_BOBA, 401)
    except Bugulma:
        return answer(BUGULMA, 200)
