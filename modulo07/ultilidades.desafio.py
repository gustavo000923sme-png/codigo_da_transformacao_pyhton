from faker import Faker

# Importa os seus outros dois arquivos renomeados
import utilidades
import utilidades_licao2

# Atividade 1: Testando a matemática
print("=== 1. MATEMÁTICA ===")
print("Soma (10 + 5):", utilidades.somar(10, 5))
print("Potência (2 ^ 3):", utilidades.potencia(2, 3))
print()

# Atividade 2: Biblioteca externa (Faker)
print("=== 2. GERADOR DE DADOS (FAKER) ===")
fake = Faker('pt_BR')
print("Nome:", fake.name())
print("Email:", fake.email())
print("Cidade:", fake.city())
print()

# Atividade 3: Executando o jogo do outro arquivo
utilidades_licao2.jogar()