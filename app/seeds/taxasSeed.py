from flask_seeder import Seeder
#from mongoengine import Document
import json
from models.TaxasModel import TaxaModel

class TaxaSeeder(Seeder):

    def ler_json(self, arq_json):
        with open(arq_json, 'r', encoding='utf8') as f:
            return json.load(f)

    def run(self):
        data = self.ler_json("./seeds/taxas.json")
        for d in data:
            #print(d)
            mod = TaxaModel(tipo=d['tipo'], taxas=d['taxas'])
            mod.save()
            #print("inserte", mod.to_json)
