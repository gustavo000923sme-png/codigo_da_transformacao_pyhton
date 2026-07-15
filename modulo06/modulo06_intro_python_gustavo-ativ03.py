'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''

import csv

lista_notas = [
    ["Nome", "Nota1", "Nota2"], 
    ["Ana", "8.5", "9.0"],
    ["Bruno", "7.0", "6.5"],
    ["Carla", "9.5", "10.0"]
]

with open("notas_alunos.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=";") 
    escritor.writerows(lista_notas)
print("Dados de notas salvos em notas_alunos.csv!")

print("\n--- Conteúdo carregado do CSV ---")
with open("notas_alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=";")
    for linha in leitor:
        print(f"Aluno: {linha[0]} | Notas: {linha[1:] if linha[1:] else 'Sem notas'}")