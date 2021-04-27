from flask import Flask, jsonify, render_template
import sys, os 
import http_response
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
    return "api de identificação"

@app.route('/login', methods=['POST'])
def login():
    pass

@app.route('/cadastra', methods=['POST'])
def cadastra():
    pass

@app.route('/edita', methods=['PUT'])
def edita():
    pass

@app.route('/deleta', methods=['DELETE'])
def deleta():
    pass


app.register_error_handler(404, http_response.invalid_route)
app.register_error_handler(405, http_response.method_allowed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)