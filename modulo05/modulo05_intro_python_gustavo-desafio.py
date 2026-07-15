'''

Módulo 05 - Funções em python
neste módulo, eu irei fazer 3 exercícios de funções em python

'''

banco_usuarios = {
    "admin": "12345",
    "joao_silva": "senhaSegura99",
    "ana_clara": "python_eh_vida"
}

def validar_login(usuario, senha):
    
    if usuario in banco_usuarios:
     
        if banco_usuarios[usuario] == senha:
            print(f"Login bem-sucedido! Bem-vindo, {usuario}!")
            return True
        else:
            print("Senha incorreta!")
            return False
    else:
        print("Usuário não cadastrado!")
        return False

# Exemplos de uso:
print("--- Teste 1: Dados corretos ---")
validar_login("joao_silva", "senhaSegura99")

print("\n--- Teste 2: Senha errada ---")
validar_login("admin", "senha_errada")

print("\n--- Teste 3: Usuário inexistente ---")
validar_login("marcos", "123")