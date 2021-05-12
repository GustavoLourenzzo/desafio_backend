from flask_seeder import Seeder
import json
from models.UsersModel import UserModel

class UserSeeder(Seeder):

    def ler_json(self, arq_json):
        with open(arq_json, 'r', encoding='utf8') as f:
            return json.load(f)


    def run(self):
        data = self.ler_json("./seeds/clientes.json")
        print("inserindo ...")
        for d in data:
            #print(d)
            mod = UserModel(
                nome=str(d['nome']),
                cpf=str(d['cpf']),
                celular=str(d['celular']),
                negativado=d['negativado'],
                score=d['score']
            )
            
            #print(mod.to_json())
            mod.save()
        print("Concluido")