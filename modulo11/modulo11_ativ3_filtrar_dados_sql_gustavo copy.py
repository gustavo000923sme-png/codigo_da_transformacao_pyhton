'''
Módulo 11 - Banco de dados com SQLite
'''

import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Amanda Lima", "amanda@email.com"))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Bruno Alves", "bruno@email.com"))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ("Antônio Pedro", "antonio@email.com"))
conexao.commit()


print("--- Clientes com nome começando em 'A' ---")
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")

clientes_com_a = cursor.fetchall()
for cliente in clientes_com_a:
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

conexao.close()