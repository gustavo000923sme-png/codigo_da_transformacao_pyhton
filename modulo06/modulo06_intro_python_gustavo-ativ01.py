'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''


conteudo_para_salvar = "Olá! Este é um texto de teste armazenado em um arquivo TXT usando Python."

#Usamos o with para ele abrir nossa pasta de dados.txt, com o nome de
#conteudo_para_salvar para salvar o contúdo dentro do arquivo txt.

with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_para_salvar)
print("Arquivo TXT criado e salvo com sucesso!")

#Aqui é oque o arquivo vai fazer, ponto da uma função como o .read que 
#lê o arquivo para a proxima função mostrar oque tem escrito nele.

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo_lido = arquivo.read()

#Na linha 24 e 25 ele mostra o conteudo lido dentro do arquivo txt que
#criamos a cima mostrando todas as informações que contem dentro do 
#arquivo mostrado.

print("\n--- Conteúdo lido do arquivo TXT ---")
print(conteudo_lido)