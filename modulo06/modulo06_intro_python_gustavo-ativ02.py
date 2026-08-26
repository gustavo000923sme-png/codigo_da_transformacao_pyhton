'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''
#O import json faz com que carregue o módulo nativo no formato json
#(JavaScript Object Notation) que é um dos formatos mais usados para
#trocar informações na web para salvar dados de configurações.

import json

#Aqui mostra os clientes que serão usados como exemplos com nome e-mail etc

clientes = {
    "cliente_1": {"nome": "Carlos Souza", "email": "carlos@email.com", "ativo": True},
    "cliente_2": {"nome": "Beatriz Lima", "email": "beatriz@email.com", "ativo": False}
}
#Aqui abre os arquivos dos clientes usando o json e jogando com .dump tudo para  o arquivo json
#depis ele é aberto e mostra os dados que carregamos durante o json, no final os dados carregados 
#são mostrados.

with open("clientes.json", "w", encoding="utf-8") as arquivo_json:

    json.dump(clientes, arquivo_json, indent=4, ensure_ascii=False)
print("Dicionário salvo em clientes.json!")

with open("clientes.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json)

print("\n--- Dados carregados do JSON ---")
print(dados_carregados)