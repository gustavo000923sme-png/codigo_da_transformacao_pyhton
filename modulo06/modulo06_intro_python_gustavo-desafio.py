'''

Módulo 06 - Manipulação de arquivos em python
neste módulo, eu irei fazer 3 exercícios de manipulação de arquivos em python

'''
#o Shutil faz com que copie e crie um backup dos arquivos mostrados, com a diferença do os que 
#verifica sem tem algo para apagar durante os backups.

import shutil
import os

arquivo_origem = "dados.txt" 
pasta_backup = "backup_destino"

#Aqui o os esta verficando se tem algo na pasta, e se caso tenha ira para a pasta backup
#caso não tenha ele ira criar uma pasta para mandar as coisas.

if not os.path.exists(pasta_backup):
    os.makedirs(pasta_backup)

caminho_destino = os.path.join(pasta_backup, arquivo_origem)

#Aqui leva o arquivo criado para o arquivo de origem, caminho do destino. Caso estiver indo para o 
#lugar certo ele será levado para o caminho_destino, caso a pasta não exista será levado para o
#arquivo de origem.

try:
    shutil.copy2(arquivo_origem, caminho_destino)
    print(f"Backup realizado com sucesso! Arquivo copiado para: '{caminho_destino}'")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado para fazer o backup. Execute a atividade 1 primeiro!")