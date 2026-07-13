'''

Módulo 04 - Estruturas de dados
Neste módulo, eu irei fazer 3 exercícios de estruturas de dados
neste eu irei fazer uma lista

'''

lista_compras = []

while True:
    print("\n--- MENU LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    if opcao == "1":
        item = input("Digite o nome do item para adicionar: ")
        lista_compras.append(item)
        print(f"'{item}' foi adicionado com sucesso!")
        
    elif opcao == "2":
        if len(lista_compras) == 0:
            print("Sua lista está vazia. Não há nada para remover.")
        else:
            item = input("Digite o nome do item para remover: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"'{item}' foi removido com sucesso!")
            else:
                print("Esse item não está na lista.")
                
    elif opcao == "3":
        print("\n--- Sua Lista Atual ---")
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
                
    elif opcao == "4":
        print("Saindo do programa. Boas compras!")
        break
    else:
        print("Opção inválida! Tente novamente.")