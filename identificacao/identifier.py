from flask import Flask, jsonify, render_template, request, Response
import sys, os , json
import http_response
from utils import Utils
from flask_mongoengine import MongoEngine
from models.UsersModel import UserModel

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'desafio_back',
    'host': 'mongo',
    'port': 27017,
    'username': 'root',
    'password': 'senha123',
    'authentication_source': 'admin'
   
}

db = MongoEngine()
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    #return jsonify({"algo": sys.path})
    return render_template('read-me.html')

@app.route('/get-user', methods=['GET'])
def login():
    utils = Utils()
    data = request.args
    if "cpf" in data:
        if not utils.validaCpf(data['cpf']):
            return http_response.bad_request(["O campo 'cpf' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'cpf' não foi enviado."])
    
    if "celular" in data:
        if not utils.validaCelular(data['celular']):
            return http_response.bad_request(["O campo 'celular' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'celular' não foi enviado."])

    cpf = utils.cpfViewToData(data['cpf'])
    celular = utils.celularViewToData(data['celular'])

    user = UserModel.objects(cpf=cpf, celular=celular).first()
    if not user:
        return http_response.forbidden()
    
    return http_response.success_200(user.to_dict())


@app.route('/cadastra', methods=['POST'])
def cadastra():
    utils = Utils()
    data = json.loads(request.data)
    #confere o campo cpf
    if "cpf" in data:
        if not utils.validaCpf(data['cpf'], True):
            return http_response.bad_request(["O campo 'cpf' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'cpf' não foi enviado."])
    
    #confere o campo celular
    if "celular" in data:
        if not utils.validaCelular(data['celular']):
            return http_response.bad_request(["O campo 'celular' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'celular' não foi enviado."])

    #confere o campo nome
    if "nome" in data:
        if len(data['nome']) < 4:
            return http_response.bad_request(["O campo 'nome' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'nome' não foi enviado."])

    #confere o campo score
    if "score" in data:
        if not utils.validaScore(data['score']):
            return http_response.bad_request(["O campo 'score' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'score' não foi enviado."])
    
    #confere o campo negativado
    if "negativado" in data:
        if not isinstance(data['negativado'], bool):
            return http_response.bad_request(["O campo 'negativado' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'negativado' não foi enviado."])

    newUser = UserModel(nome=data['nome'],
            cpf=utils.cpfViewToData(data['cpf']),
            celular=utils.celularViewToData(data['celular']),
            negativado=data['negativado'],
            score=data['score'])

    newUser.save()
    return http_response.success_201()


@app.route('/edita', methods=['PUT'])
def edita():
    utils = Utils()
    data = json.loads(request.data)
    
    if "cpf" in data:
        if not utils.validaCpf(data['cpf'], True):
            return http_response.bad_request(["O campo 'cpf' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'cpf' não foi enviado."])
    
    
    if "celular" in data:
        if not utils.validaCelular(data['celular']):
            return http_response.bad_request(["O campo 'celular' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'celular' não foi enviado."])

    cpf = utils.cpfViewToData(data['cpf'])
    celular = utils.celularViewToData(data['celular'])

    user = UserModel.objects(cpf=cpf, celular=celular).first()
    if not user:
        return http_response.forbidden()

    if "nome" in data:
        if len(data['nome']) < 4:
            return http_response.bad_request(["O campo 'nome' não possui um valor válido"])
        else:
            user.setNome(data['nome'])

    if "score" in data:
        if not utils.validaScore(data['score']):
            return http_response.bad_request(["O campo 'score' não possui um valor válido"])
        else:
            user.setScore(data['score'])
    
    if "negativado" in data:
        if not isinstance(data['negativado'], bool):
            return http_response.bad_request(["O campo 'negativado' não possui um valor válido"])
        else:
            user.setNegativado(data['negativado'])

    user.save()
    return http_response.success_200("Registro atualizado com sucesso")


@app.route('/deleta', methods=['DELETE'])
def deleta():
    utils = Utils()
    data = json.loads(request.data)
    
    if "cpf" in data:
        if not utils.validaCpf(data['cpf'], True):
            return http_response.bad_request(["O campo 'cpf' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'cpf' não foi enviado."])
    
    
    if "celular" in data:
        if not utils.validaCelular(data['celular']):
            return http_response.bad_request(["O campo 'celular' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'celular' não foi enviado."])

    cpf = utils.cpfViewToData(data['cpf'])
    celular = utils.celularViewToData(data['celular'])

    user = UserModel.objects(cpf=cpf, celular=celular).first()
    if not user:
        return http_response.forbidden()
    
    user.delete()
    return http_response.success_200("Registro deletado com sucesso")



app.register_error_handler(404, http_response.invalid_route)
app.register_error_handler(405, http_response.method_allowed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)