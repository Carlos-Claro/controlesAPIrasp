import datetime

from connexion import NoContent

import serial
import json


condicao = {
    "dht11":
        {
            "humidade": 1.0,
            "temperatura": 11.1,
            "temperatura_sensacao": 11.1
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
    condicao = get_temperatura()
    return condicao, 200

def get_temperatura():
    comunicacao = serial.Serial('/dev/ttyUSB0', 9600)
    try:
        condicao = comunicacao.readline().decode('utf-8')
    except (OSError, serial.SerialException):
        pass
    return condicao

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
    condicao = get_temperatura()
    return condicao,200