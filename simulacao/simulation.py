from flask import Flask, jsonify, request,Response,render_template
import sys, os, math,json
import http_response
from utils import Utils
from flask_mongoengine import MongoEngine
from models.TaxasModel import TaxaModel
from flask_cors import CORS


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
CORS(app)

@app.route('/', methods=['GET'])
def index():
    
    return render_template('read-me.html')

#Função que retorna a taxa de juros com base no perfil e numero de parcelas.
@app.route('/get-taxa', methods=['GET'])
def getTaxa():
    data = request.args
    ut = Utils()
    if "tipo" in data:
        if not ut.checkEnumTipoTaxa(data['tipo']):
            return http_response.bad_request(["O campo 'tipo' contem o valor inválido."])
    else:
        return http_response.bad_request(["O campo 'tipo' não foi enviado."])

    if "numeroParcelas" in data:
        if not ut.checkEnumParcelas(int(data['numeroParcelas'])):
            return http_response.bad_request(["O campo 'numeroParcelas' contem o valor inválido."])
    else:
        return http_response.bad_request(["O campo 'numeroParcelas' não foi enviado."])

    taxa = TaxaModel.objects(tipo=data['tipo']).first()
    if not taxa:
        return http_response.forbidden()
    
    return http_response.success_200(taxa.to_dict()['taxas'][data['numeroParcelas']])



@app.route('/calculo', methods=['POST'])
def calculaSimulacao():
    data = json.loads(request.data)
    #return http_response.success_200(data)
    ut = Utils()
    if "valor" in data:
        if not (isinstance(data['valor'], int) or isinstance(data['valor'], float)):
            return http_response.bad_request(["O campo 'valor' não e um numero (Natural / Real)."])
        if float(data['valor']) < 1.0:
            return http_response.bad_request(["O campo 'valor' não possui um valor válido"])
    else:
        return http_response.bad_request(["O campo 'valor' não foi enviado."])    

    if "numeroParcelas" in data:
        if not ut.checkEnumParcelas(int(data['numeroParcelas'])):
            return http_response.bad_request(["O campo 'numeroParcelas' contem o valor inválido."])
    else:
        return http_response.bad_request(["O campo 'numeroParcelas' não foi enviado."])

    if "taxaJuros" in data:
        if not (isinstance(data['taxaJuros'], float)):
            return http_response.bad_request(["O campo 'taxaJuros' não e uma taxa válida."])
    else:
        return http_response.bad_request(["O campo 'taxaJuros' não foi enviado."])
    
    montante = round(float(data['valor']) * ((1+ float(data['taxaJuros']))**int(data['numeroParcelas'])), 2)

    ret = {}

    ret['total_parcela'] = round(montante / int(data['numeroParcelas']), 2)
    ret['total'] = ret['total_parcela'] *  int(data['numeroParcelas'])

    #return http_response.success_200("ok")
    return http_response.success_200(ret)



app.register_error_handler(404, http_response.invalid_route)
app.register_error_handler(405, http_response.method_allowed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)