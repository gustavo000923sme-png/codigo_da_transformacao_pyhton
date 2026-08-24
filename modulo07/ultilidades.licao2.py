'''Aula 7 - Módulos e pacotes
Nesse módulo iremos fazer um arquivo chamado ultilodades.py para completar as atividades
'''

import random
import math
from faker import Faker


import utilidades

print("=== ATIVIDADE 1: Testando utilidades.py ===")
print("Soma (10 + 5):", utilidades.somar(10, 5))
print("Subtração (10 - 5):", l.subtrair(10, 5))
print("Potência (2 ^ 3):", utilidades.potencia(2, 3))
print()


print("=== ATIVIDADE 2: Biblioteca Faker ===")
fake = Faker('pt_BR')
print("Nome gerado:", fake.name())
print("Email gerado:", fake.email())
print("Cidade:", fake.city())
print()


print("=== ATIVIDADE 3: Jogo de Adivinhação ===")
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Adivinhe o número secreto entre 1 e 100!")

while not acertou:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1
    
 
    diferenca = int(math.fabs(numero_secreto - chute))
    
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!\n")
        acertou = True
    elif chute < numero_secreto:
        print(f"Tente um número MAIOR. (Diferença de {diferenca})")
    else:
        print(f"Tente um número MENOR. (Diferença de {diferenca})")