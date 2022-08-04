from flask import Flask 
from flask_restx import Api, Resource 
import json
from src.server.instance import server
from flask.json import jsonify


app, api = server.app, server.api


with open('dados.json', encoding='utf8') as dadosjson:
    data = json.load(dadosjson)
print(type(data))

def underline(x):
    return x.replace(" ","_")


@app.route('/propostas', methods=['GET'])
def propostas():
    return jsonify(data["dados"])

@app.route('/propostas/tipo/<tipo>', methods=['GET'])
def propostas_tipo(tipo):
    propostas_por_tipo = []
    for proposta in (data["dados"]):
        if (underline(proposta["descricaoTipo"]) == tipo):
            propostas_por_tipo.append(proposta)
    return jsonify(propostas_por_tipo)

@app.route('/propostas/autor/<autores>', methods=['GET'])
def propostas_autores(autores):
    lista_autores = []
    for proposta in (data["dados"]):
        for author in range(len(proposta["autores"])):
            if (underline(proposta["autores"][author]["nomeAutor"]) == autores):
                lista_autores.append(proposta) 
    return jsonify(lista_autores)
