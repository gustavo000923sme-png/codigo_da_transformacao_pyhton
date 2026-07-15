'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''


conteudo_para_salvar = "Olá! Este é um texto de teste armazenado em um arquivo TXT usando Python."

with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_para_salvar)
print("Arquivo TXT criado e salvo com sucesso!")


with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo_lido = arquivo.read()

print("\n--- Conteúdo lido do arquivo TXT ---")
print(conteudo_lido)