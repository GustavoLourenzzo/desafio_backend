from mongoengine import Document, StringField, BooleanField, IntField
import json

class UserModel(Document):
    nome = StringField(required=True, max_length=100)
    cpf = StringField(required=True, max_length=20, min_length=11)
    celular = StringField(max_length=25)
    negativado = BooleanField()
    score = IntField(min_value=0, max_value=1000)

    

    def to_json(self):
        return json.dump({
            "nome": self.nome,
            "cpf":self.cpf,
            "celular":self.celular,
            "negativado":self.negativado,
            "score":self.score
        }); 


