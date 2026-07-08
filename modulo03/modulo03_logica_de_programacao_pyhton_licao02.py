'''
Módulo 03 - Lógica de programação em python

'''

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Compara qual é maior
if n1 > n2:
    print(f"O maior número é o primeiro: {n1}")
elif n2 > n1:
    print(f"O maior número é o segundo: {n2}")
else:
    print("Os dois números são iguais!")