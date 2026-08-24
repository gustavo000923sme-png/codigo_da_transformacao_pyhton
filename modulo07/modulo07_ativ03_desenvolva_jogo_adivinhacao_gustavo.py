'''
Módulo 07 - Jogo da adivinhação (Modo Difícil)
'''
import random

numero_secreto = random.randint(1, 100)
tentativas = 0
limite_tentativas = 7
acertou = False

print("=== JOGO DA ADIVINHAÇÃO - MODO DIFÍCIL ===")
print(f"Adivinhe o número secreto entre 1 e 100! Você tem {limite_tentativas} tentativas.\n")

while not acertou and tentativas < limite_tentativas:
    try:
        chute = int(input(f"Tentativa {tentativas + 1}/{limite_tentativas} - Digite seu palpite: "))
    except ValueError:
        print("Por favor, digite apenas números inteiros válidos.\n")
        continue

    if chute < 1 or chute > 100:
        print("Atenção: O número deve estar entre 1 e 100!\n")
        continue

    tentativas += 1
    diferenca = abs(numero_secreto - chute)

    if chute == numero_secreto:
        print(f"\nParabéns! Você venceu e acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        acertou = True
    else:
        # Pista baseada na proximidade em vez do número exato
        if diferenca <= 3:
            pista = "FERVENDO!"
        elif diferenca <= 10:
            pista = "Quente!"
        elif diferenca <= 20:
            pista = "Morno."
        else:
            pista = "Frio..."

        direcao = "MAIOR" if chute < numero_secreto else "MENOR"
        print(f"Tente um número {direcao}. Pista: {pista}\n")

if not acertou:
    print(f"\nGame Over! Suas {limite_tentativas} tentativas acabaram. O número secreto era {numero_secreto}.")