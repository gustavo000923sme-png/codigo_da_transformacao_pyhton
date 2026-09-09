'''
Módulo 11 - Banco de dados com SQLite
'''

import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    status TEXT DEFAULT 'Pendente'
)
""")
conexao.commit()


def adicionar_tarefa(descricao):
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    print(f"📌 Tarefa '{descricao}' adicionada!")

def visualizar_tarefas():
    print("\n--- Lista de Tarefas ---")
    cursor.execute("SELECT * FROM Tarefas")
    for t in cursor.fetchall():
        print(f"ID: {t[0]} | Descrição: {t[1]} | Status: {t[2]}")


def excluir_tarefa(id_tarefa):
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    print(f"🗑️ Tarefa ID {id_tarefa} excluída!")


adicionar_tarefa("Estudar SQL")
adicionar_tarefa("Fazer o exercício da aula")
visualizar_tarefas()

excluir_tarefa(1)
visualizar_tarefas()

conexao.close()