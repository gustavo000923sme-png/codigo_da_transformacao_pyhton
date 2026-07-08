'''
Módulo 03 - Lógica de programação em python

'''

idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Categoria: Criança")
elif idade < 18:
    print("Categoria: Adolescente")
elif idade < 60:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")