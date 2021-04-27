from mongoengine import Document, StringField, DictField
import json

class TaxaModel(Document):
    tipo = StringField(required=True)
    taxas = DictField(required=True)

    def to_json(self):
        return json.dump({
            "tipo": self.tipo,
            "taxas":self.taxas
        }); 

