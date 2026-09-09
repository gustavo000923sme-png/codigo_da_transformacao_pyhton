'''
Módulo 11 - Banco de dados com SQLite
'''

import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conexao.commit()
conexao.close()
print("Tabela 'Clientes' criada com sucesso!")