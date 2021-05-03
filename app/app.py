from flask import Flask, jsonify, render_template, request, Response
import sys, os , json, requests as http
import http_response
from flask_seeder import FlaskSeeder
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from utils import Utils

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'desafio_back',
    'host': 'mongo',
    'port': 27017,
    'username': 'root',
    'password': 'senha123',
    'authentication_source': 'admin'
   
}
## apis urls
API_SIMULACAO = "http://simulacao:5000"
API_IDENTIFICACAO = "http://identificacao:5000"

db = MongoEngine()
db.init_app(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)

CORS(app)

@app.route('/',methods=['GET'])
def index():
    #return jsonify({"algo": sys.path})
    return render_template('read-me.html')
    
@app.route('/simulacao', methods=['POST'])
def simulacao():
    try:
        dataObj = json.loads(request.data)
        
        if "valor" in dataObj:
            if not (isinstance(dataObj['valor'], int) or isinstance(dataObj['valor'], float)):
                return http_response.bad_request(["O campo 'valor' não e um numero (Natural / Real)."])
            if float(dataObj['valor']) < 1.0:
                return http_response.bad_request(["O campo 'valor' não possui um valor válido"])
        else:
            return http_response.bad_request(["O campo 'valor' não foi enviado."])
        
        if "numeroParcelas" not in dataObj:
            return http_response.bad_request(["O campo 'numeroParcelas' não foi enviado."])
        ut = Utils()
        if "user" in dataObj:
            r = http.get(
                API_SIMULACAO+"/get-taxa",
                params={
                    "tipo": ut.getPerfilScore(
                        dataObj['user']['score'],
                        dataObj['user']['negativado']
                    ),
                    "numeroParcelas":dataObj['numeroParcelas'] 
                }
            )
        else:
            r = http.get(API_SIMULACAO+"/get-taxa", params={"tipo": ut.getPerfilScore(0, False),"numeroParcelas":dataObj['numeroParcelas'] })
        
        taxaObj = json.loads(r.content)
        if r.status_code == 400:
            return http_response.bad_request(taxaObj['result']['error']['errors'])
        if r.status_code == 403:
            return http_response.forbidden()

        rt = http.post(url=API_SIMULACAO+"/calculo", data=json.dumps({'valor' : dataObj['valor'], "numeroParcelas" : dataObj['numeroParcelas'], "taxaJuros": taxaObj['result'] }))
        calcObj = json.loads(rt.content)
        if rt.status_code != 200:
            return http_response.internalError()
        
        calcObj['result']['taxa'] = taxaObj['result']
        calcObj['result']['v_inicial'] = dataObj['valor']
        calcObj['result']['qtd_parcelas'] = dataObj['numeroParcelas']
        return http_response.success_200(calcObj['result'])

    except:
        return http_response.internalError()
        #return http_response.success_200(rt.status_code)

@app.route('/login', methods=['POST'])
def login():
    dataObj = json.loads(request.data)
    if "cpf" not in dataObj:
        return http_response.bad_request(["O campo 'cpf' não foi enviado."])
    if "celular" not in dataObj:
        return http_response.bad_request(["O campo 'celular' não foi enviado."])

    r = http.get(API_IDENTIFICACAO+"/get-user", params={"cpf": dataObj['cpf'],"celular":dataObj['celular'] })
    userObj = json.loads(r.content)
    if r.status_code == 400:
        return http_response.bad_request(userObj['result']['error']['errors'])
    if r.status_code == 403:
            return http_response.forbidden()
    
    return http_response.success_200(userObj['result'])



@app.route('/usuario/cadastrar', methods=['POST'])
def cadastrar():
    dataObj = json.loads(request.data)
    rt = http.post(url=API_IDENTIFICACAO+"/cadastra", data=json.dumps(dataObj))
    userObj = json.loads(rt.content)
    if rt.status_code == 400:
        return http_response.bad_request(userObj['result']['error']['errors'])
    return http_response.success_200(userObj['result'])

@app.route('/usuario/editar', methods=['PUT'])
def editar():
    dataObj = json.loads(request.data)
    rt = http.put(url=API_IDENTIFICACAO+"/edita", data=json.dumps(dataObj))
    userObj = json.loads(rt.content)
    if rt.status_code == 400:
        return http_response.bad_request(userObj['result']['error']['errors'])
    if rt.status_code == 403:
            return http_response.forbidden()
    return http_response.success_200(userObj['result'])


@app.route('/usuario/deletar', methods=['DELETE'])
def deletar():
    dataObj = json.loads(request.data)
    if "cpf" not in dataObj:
        return http_response.bad_request(["O campo 'cpf' não foi enviado."])
    if "celular" not in dataObj:
        return http_response.bad_request(["O campo 'celular' não foi enviado."])
    rt = http.delete(url=API_IDENTIFICACAO+"/deleta", data=json.dumps(dataObj))
    userObj = json.loads(rt.content)
    if rt.status_code == 400:
        return http_response.bad_request(userObj['result']['error']['errors'])
    if rt.status_code == 403:
            return http_response.forbidden()
    return http_response.success_200(userObj['result'])


app.register_error_handler(404, http_response.invalid_route)
app.register_error_handler(405, http_response.method_allowed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)