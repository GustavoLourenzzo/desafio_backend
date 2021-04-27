from flask import Response, jsonify


def bad_request() -> Response:
    output = {
        "error":{
            "msg": "400 error: Requisição inválida."
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
              {"msg": "403 error: Requisição não autorizada."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 403
    return resp


def invalid_route(e) -> Response:
    output = {"error":
              {"msg": "404 error: Rota não suportada."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp

