from faker import Faker


import ultilidades
import ultilidades_licao2


print("=== 1. MATEMÁTICA ===")
print("Soma (10 + 5):", ultilidades.somar(10, 5))
print("Potência (2 ^ 3):", ultilidades.potencia(2, 3))
print()


print("=== 2. GERADOR DE DADOS (FAKER) ===")
fake = Faker('pt_BR')
print("Nome:", fake.name())
print("Email:", fake.email())
print("Cidade:", fake.city())
print()

# Atividade 3: Executando o jogo do outro arquivo
ultilidades_licao2.jogar()