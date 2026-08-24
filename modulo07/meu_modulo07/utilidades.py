'''Aula 07 - Módulos e pacotes" 
Nesse módulo iremos fazer um arquivo chamado ultilodades.py para completar as atividades
'''

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def potencia(base, expoente):
    return base ** expoente

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b 

def resto_divisao(a, b):

  if b == 0:
      return "Erro: Divisão por zero não é permitida."
  return a % b 

def calcular_medida(lista_numeros):
    if not lista_numeros:
        return 0 
    return sum(lista_numeros) / len(lista_numeros)

def e_par(numero):
    return numero % 2 == 0