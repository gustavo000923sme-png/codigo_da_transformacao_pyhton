'''
Módulo 08 - Módulos e Pacotes
 Neste módulo, irei fazer 3 exercícios e um desafio de manipulação de arquivos em python,
ultilizando módulos e pacotes, para organizar melhor o código e facilitar a mantenção
do mesmo.
'''
#estudar mais sobre crição de perfils aleatórios de pessoas para treinar
#a criação de perfils de qualquer coisa.
from faker import Faker

fake = Faker('pt_BR')

print("=== Criador de perfil de pessoas aleatórias ===")

for i in range(1, 4):
    print(f"\n--- Perfil {i} ---")
    print("Nome:", fake.name())
    print("Data de Nascimento:", fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y'))
    print("Gênero:", fake.random_element(elements=('Masculino', 'Feminino')))
    print("CPF:", fake.cpf())
    print("RG:", fake.rg())
    print("Profissão:", fake.job())
    print("Email:", fake.email())
    print("Telefone:", fake.cellphone_number())
    print("Endereço:", fake.address().replace('\n', ', '))
    print("Cidade:", fake.city())
    print("Estado:", fake.state_abbr())
    print("CEP:", fake.postcode())
    print("Nacionalidade:", fake.country())
    print("-----------------------------")