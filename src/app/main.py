import sys
import os

# Caminho absoluto do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Voltar atras no caminho absoluto (src)
sys.path.append(os.path.join(current_dir, '..'))

# Importar o create/insert, read e delete
from create.create_tables import create_tables
from read.read_alunos import read_alunos
from delete.delete_aluno import delete_aluno

if __name__ == "__main__":
    #enquanto estiver a correr
    while True:
        print("\nMenu:")
        print("1. Adicionar Aluno")
        print("2. Mostrar Alunos")
        print("3. Apagar Aluno")
        print("4. Sair")

        choice = input("Escolha uma opção (1-4): ")

        #ações feitas baseado no input
        if choice == '1':
            create_tables()
        elif choice == '2':
            read_alunos()
        elif choice == '3':
            student_id = input("Escreva o id do aluno para apagar: ")
            delete_aluno(student_id)
        elif choice == '4':
            print("A sair")
            break
        else:
            print("Inválido")