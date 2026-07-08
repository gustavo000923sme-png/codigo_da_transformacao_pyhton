'''
Módulo 03 - Lógica de programação em python

'''

while True:
    print("\n--- MENU ---")
    print("1. Soma")
    print("2. Subtracao")
    print("3. Sair")
    
    opcao = input("Escolha (1, 2 ou 3): ")
    
    if opcao == "1":
        n1 = float(input("Numero 1: "))
        n2 = float(input("Numero 2: "))
        print("Resultado:", n1 + n2)
        
    elif opcao == "2":
        n1 = float(input("Numero 1: "))
        n2 = float(input("Numero 2: "))
        print("Resultado:", n1 - n2)
        
    elif opcao == "3":
        print("Saindo...")
        break  # Esse comando para o programa
        
    else:
        print("Opcao invalida!")