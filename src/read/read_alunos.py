import sqlite3
def read_alunos():
    # Conectar ao banco de dados
    conexao = sqlite3.connect("DaB.db")
    cursor = conexao.cursor()

    # Selecionar todos os dados da tabela 'alunos'
    cursor.execute('SELECT * FROM aluno')
    resultados = cursor.fetchall()

    # Imprimir cada registro
    for registro in resultados:
        print(registro)

    # Fechar a conexão
    conexao.close()