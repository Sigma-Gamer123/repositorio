import sqlite3
def delete_aluno(student_id):
    # Connect to the database
    conexao = sqlite3.connect('DaB.db')
    cursor = conexao.cursor()

    # Find the id_aluno of the student to be deleted
    cursor.execute("SELECT id_aluno FROM aluno WHERE id_aluno = ?", (student_id,))
    student = cursor.fetchone()

    # Check if student exists
    if student:
        # Delete the student from the aluno table
        cursor.execute("DELETE FROM aluno WHERE id_aluno = ?", (student_id,))
        # Commit changes
        conexao.commit()
        print(f"Aluno associado ao id '{student_id}' foi apagado.")
    else:
        print(f"Aluno de id '{student_id}' não encontrado.")

    # Close the connection
    conexao.close()