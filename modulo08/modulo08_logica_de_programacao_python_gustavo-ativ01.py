'''
Módulo 08 - Módulos e Pacotes
 Neste módulo, irei fazer 3 exercícios e um desafio de manipulação de arquivos em python,
ultilizando módulos e pacotes, para organizar melhor o código e facilitar a mantenção
do mesmo.
'''

print("Qual é a operação desejada?")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")


def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  if b == 0:
    raise ValueError("Divisão por zero não é permitida.")
  return a / b

def potencia(base, expoente):
  return base ** expoente

opcao = input("Digite o número da opção: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("Resultado:", soma(num1, num2))
elif opcao == "2":
    print("Resultado:", subtracao(num1, num2))
elif opcao == "3":
    print("Resultado:", multiplicacao(num1, num2))
elif opcao == "4":
    print("Resultado:", divisao(num1, num2))
elif opcao == "5":
    print("Resultado:", potencia(num1, num2))
else:
    print("Opção inválida!")