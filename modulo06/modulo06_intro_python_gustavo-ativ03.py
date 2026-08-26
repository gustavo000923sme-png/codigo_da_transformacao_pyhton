'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''
# O import CSV serve para ler e escrever\estruturar arquivosque é o padrão de planilhas e excel.

import csv

#Mostra uma lista com nome e notas das pessoas ficticias.

lista_notas = [
    ["Nome", "Nota1", "Nota2"], 
    ["Ana", "8.5", "9.0"],
    ["Bruno", "7.0", "6.5"],
    ["Carla", "9.5", "10.0"]
]

#Aqui abre o arquivo CSV em uma nova linha usando o arquivo_csv faz a escrita do arquivo usando as 
#informações dos alunos como nome e notas, assim salvando elas no final.

with open("notas_alunos.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=";") 
    escritor.writerows(lista_notas)
print("Dados de notas salvos em notas_alunos.csv!")

print("\n--- Conteúdo carregado do CSV ---")
#Aqui apenas carrega o nome e as notas do aluno que foram salvas durante o código assim colocando um
#print para mostrar as notas, nome dos alunos e caso ele n tenha nota.

with open("notas_alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=";")
    for linha in leitor:
        print(f"Aluno: {linha[0]} | Notas: {linha[1:] if linha[1:] else 'Sem notas'}")