'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''

import json

clientes = {
    "cliente_1": {"nome": "Carlos Souza", "email": "carlos@email.com", "ativo": True},
    "cliente_2": {"nome": "Beatriz Lima", "email": "beatriz@email.com", "ativo": False}
}

with open("clientes.json", "w", encoding="utf-8") as arquivo_json:
    # indent=4 serve para deixar o arquivo visualmente organizado ("bonito")
    json.dump(clientes, arquivo_json, indent=4, ensure_ascii=False)
print("Dicionário salvo em clientes.json!")

with open("clientes.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json)

print("\n--- Dados carregados do JSON ---")
print(dados_carregados)