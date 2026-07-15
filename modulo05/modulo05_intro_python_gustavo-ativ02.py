'''

Módulo 05 - Funções em python
neste módulo, eu irei fazer 3 exercícios de funções em python

'''

def calcular_media(notas):
    
    media = sum(notas) / len(notas)
    
    print(f"Média do aluno: {media:.2f}")
    
   
    if media >= 7.0:
        print("Status: Aprovado! 🎉")
    else:
        print("Status: Reprovado. 📚")


notas_do_aluno = [8.5, 6.0, 7.5]
calcular_media(notas_do_aluno)