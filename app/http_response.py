from flask import Response, jsonify
import json


def bad_request(ListErro) -> Response:
    output = {
        "error":{
            "msg": "400 error: Requisição inválida.",
            "errors": ListErro
        }
    }
    resp = jsonify({'result': output})
    resp.status_code = 400
    return resp

def unauthorized(label) -> Response:
    output = {
        "error":{
            "msg": "401 error: O campo "+label+" esta inválido ou vazio."
        }
    }
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp



def forbidden() -> Response:
    output = {"error":
              {"msg": "403 error: O registro solicitado não existe."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 403
    return resp

def internalError() -> Response:
    output = {"error":
              {"msg": "500 error: Houve um problema inesperado com o servidor."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 500
    return resp


def invalid_route(e) -> Response:
    output = {"error":
              {"msg": "404 error: Rota não suportada."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp

def method_allowed(e) -> Response:
    output = {"error":
              {"msg": "405 error: Você não tem acesso a esse metodo."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 405
    return resp


def success_200(data) -> Response:
    resp = jsonify({'result': data})
    resp.status_code = 200
    return resp

def success_201() -> Response:
    resp = jsonify({'result': "Registro gravado com sucesso."})
    resp.status_code = 201
    return resp
