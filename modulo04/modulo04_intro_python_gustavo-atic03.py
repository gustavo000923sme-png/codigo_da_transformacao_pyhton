'''

Módulo 04 - Estruturas de dados
Neste módulo, eu irei fazer 3 exercícios de estruturas de dados
neste eu irei fazer um programa para separar em pares e impares

'''

numeros = [12, 7, 23, 44, 8, 15, 99, 100]

pares = []
impares = []


for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)


print(f"Números analisados: {numeros}")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")