'''

Módulo 05 - Funções em python
neste módulo, eu irei fazer 3 exercícios de funções em python

'''

def maior_menor(numeros):
    
    if not numeros:
        return None, None
        
    
    maior = max(numeros)
    menor = min(numeros)
    
    return maior, menor


lista_valores = [15, 42, 3, 89, 21, 7]
maior_val, menor_val = maior_menor(lista_valores)

print(f"O maior valor é: {maior_val}")
print(f"O menor valor é: {menor_val}")