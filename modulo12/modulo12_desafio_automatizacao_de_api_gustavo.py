'''
Módulo 12 - Testes automatizados
'''

import pytest
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/somar", methods=["POST"])
def api_somar():
    dados = request.get_json()
    
    if not dados or "a" not in dados or "b" not in dados:
        return jsonify({"erro": "Parâmetros inválidos"}), 400
        
    resultado = dados["a"] + dados["b"]
    return jsonify({"resultado": resultado}), 200



@pytest.fixture
def cliente():
    """Cria um cliente de teste do Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_api_somar_sucesso(cliente):
   
    resposta = cliente.post("/somar", json={"a": 5, "b": 10})
    assert resposta.status_code == 200
    assert resposta.get_json() == {"resultado": 15}

def test_api_somar_entrada_invalida(cliente):
  
    resposta = cliente.post("/somar", json={"a": 5})
    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()