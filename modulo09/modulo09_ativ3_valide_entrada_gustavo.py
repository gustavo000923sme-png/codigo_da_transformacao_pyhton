

def solicitar_idade_valida():
    """
    Solicita a idade do usuário e valida se a entrada é um número inteiro positivo.
    
    Retorna:
    - int: A idade validada do usuário.
    """
    while True:
        
        entrada = input("Por favor, digite a sua idade: ")
        
        try:
            
            idade = int(entrada)
            
           
            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro positivo (maior que zero).\n")
                
            
            
            return idade

        except ValueError:
           
            print("Erro: Entrada inválida! Por favor, digite apenas números inteiros.\n")



if __name__ == "__main__":
    print("--- Teste da Atividade 3: Validação de Idade ---\n")
    
   
    idade_confirmada = solicitar_idade_valida()
    
    print(f"\nSucesso! Idade de {idade_confirmada} anos registrada no sistema.")