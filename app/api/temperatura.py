import datetime

from connexion import NoContent

condicao = {
    "dht11":
        {
            "humidade": 70.9,
            "temperatura": 17.1,
            "temperatura_sensacao": 16.72
        },
    "dht122":
        {
            "humidade": 0,
            "temperatura": 0,
            "temperatura_sensacao": 0
        },
    "luminosidade":
        {
            "interna": 3,
            "externa": 1023
        },
    "higrometro":
        {
            "H1": 134,
            "H2": 546
        },
    "chuva": 615,
    "data": ''
}

def get():
    return condicao, 200


def post(body):
    name = body.get("name")
    tag = body.get("tag")
    count = len(pets)
    pet = {}
    pet['id'] = count + 1
    pet["tag"] = tag
    pet["name"] = name
    pet['last_updated'] = datetime.datetime.now()
    pets[pet['id']] = pet
    return pet, 201


def delete(id_):
    id_ = int(id_)
    if pets.get(id_) is None:
        return NoContent, 404
    del pets[id_]
    return NoContent, 204


def search():
    return condicao,200