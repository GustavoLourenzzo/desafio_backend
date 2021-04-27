from flask import Flask, jsonify
import sys, os 
import error
from flask_seeder import FlaskSeeder
from flask_mongoengine import MongoEngine

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

seeder = FlaskSeeder()
seeder.init_app(app, db)


@app.route('/',methods=['GET '])
def index():
    #return jsonify({"algo": sys.path})
    return "tudo certo"
    


app.register_error_handler(404, error.invalid_route)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)