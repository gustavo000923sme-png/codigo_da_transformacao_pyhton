'''

Módulo 04 - Estruturas de dados
Neste módulo, eu irei fazer 3 exercícios de estruturas de dados
neste eu irei fazer um desafio da plataforma!

'''

agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Mostrar todos os contatos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        agenda[nome] = telefone
        print(f"Contato de {nome} salvo com sucesso!")
        
    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato de {nome} removido.")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "3":
        nome = input("Digite o nome para buscar: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "4":
        print("\n--- Lista de Contatos ---")
        if len(agenda) == 0:
            print("A agenda está vazia.")
        else:
            for nome, telefone in agenda.items():
                print(f"Nome: {nome} | Telefone: {telefone}")
                
    elif opcao == "5":
        print("Fechando a agenda. Até logo!")
        break
    else:
        print("Opção inválida!")