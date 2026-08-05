'''
Módulo 08 - Módulos e Pacotes
 Neste módulo, irei fazer 3 exercícios e um desafio de manipulação de arquivos em python,
ultilizando módulos e pacotes, para organizar melhor o código e facilitar a mantenção
do mesmo.
'''

from pacotes.matematica import jogo_adivinhacao, soma
from pacotes.utilidades_faker import gerar_perfis

print("=== Menu Principal ===")
print("1 - Testar calculadora")
print("2 - Testar perfis fake")
print("3 - Testar jogo de adivinhação (random + math)")

opcao = input("Digite o número de opção desejada: ")

if opcao == "1":
    print("Soma 10 + 5 =", soma(10, 5))
elif opcao == "2":
    gerar_perfis(2)
elif opcao == "3":
    jogo_adivinhacao()
else:
    print("Opção inválida.")