import sqlite3
def create_tables():
    # Conectar à base de dados
    # Não precisamos do querie CREATE DATABASE porque com o sqlite3, a função connect() vai se ligar ao ficheiro dentro dos parenteses e se o ficheiro n existir, vai cria-lo
    conexao = sqlite3.connect('DaB.db')
    
    # "cursor" serve para escrever comandos de sql
    cursor = conexao.cursor()   
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    ''')
    
    cursor.execute("INSERT INTO aluno (nome, idade) VALUES ('Alice', 20)")
    cursor.execute("INSERT INTO aluno (nome, idade) VALUES ('Bob', 22)")
    cursor.execute("INSERT INTO aluno (nome, idade) VALUES ('Charlie', 19)")
    
    # Confirmar alterações e fechar a conexão
    conexao.commit()
    conexao.close()