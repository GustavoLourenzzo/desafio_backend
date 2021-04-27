//var users = require("./clientes.json");
//var taxas = require ("./taxas.json");
db.auth("root", 'senha123');

print("#Startou ----------------------------------")

db.getSiblingDB("desafio_back");

db.createUser({
    user: 'rooto',
    pwd: 'senha123',
    roles: [
        {
            role: 'readWrite',
            db: 'desafio_back',
        },
    ],
});



db.createCollection('users', { capped: false });
db.createCollection('taxas', { capped: false });

//db.users.insert(users);
db.taxas.insert([
    {
      "tipo":"NEGATIVADO",
      "taxas":{"6": 0.04, "12": 0.045, "18": 0.05, "24": 0.053, "36": 0.055}
    },
    {
      "tipo":"SCORE_ALTO",
      "taxas":{"6": 0.02, "12": 0.025, "18": 0.35, "24": 0.038, "36": 0.04}
    },
    {
      "tipo":"SCORE_BAIXO",
      "taxas":{"6": 0.03, "12": 0.035, "18": 0.45, "24": 0.048, "36": 0.05}
    }
  ]);

print("encerrou")