# Sistema de Gestão de Alunos com SQLite

Este projeto implementa um sistema simples de gestão de alunos utilizando a base de dados SQLite. Permite realizar operações como adicionar, listar e eliminar registos de alunos.

## Funcionalidades

O programa oferece um menu interativo para o utilizador, permitindo escolher entre as seguintes opções:

1. **Adicionar Aluno**: Cria tabelas e insere alunos na base de dados.
2. **Mostrar Alunos**: Exibe a lista de alunos registados.
3. **Apagar Aluno**: Elimina um aluno da base de dados com base no seu ID.
4. **Sair**: Encerra o programa.

## Estrutura do Sistema

O sistema de gestão está implementado no script `main.py`, onde o menu é apresentado e as funcionalidades são executadas com base na escolha do utilizador.

### Arquivos do Sistema:

- **main.py**: O script principal que exibe o menu interativo e executa as operações de adicionar, listar ou eliminar alunos.
- **create_tables.py**: Cria a tabela `aluno` na base de dados SQLite, se ainda não existir, e insere três alunos iniciais (Alice, Bob, Charlie).
- **delete_aluno.py**: Permite a exclusão de um aluno com base no seu ID.
- **read_alunos.py**: Exibe todos os alunos registados na base de dados.

## Estrutura da Base de Dados

A base de dados SQLite utilizada chama-se `DaB.db` e contém uma tabela chamada `aluno` com a seguinte estrutura:

- **id_aluno**: Identificador único do aluno (chave primária, autoincrement).
- **nome**: Nome do aluno.
- **idade**: Idade do aluno.

## Como Utilizar

### 1. Configuração da Base de Dados:

Antes de executar o programa, execute o script `create_tables.py` para garantir que a tabela `aluno` está criada e que os dados iniciais sejam inseridos na base de dados.
Também pode, após executar o programa, selecionar a primeira opção.

### 2. Executar o Sistema:

Para interagir com o sistema, execute o script `main.py`. O programa apresentará um menu com as opções disponíveis.

### 3. Eliminar um Aluno:

Para eliminar um aluno, execute o script `delete_aluno.py` e forneça o ID do aluno que pretende remover.

### 4. Listar Alunos:

O script `read_alunos.py` pode ser executado para listar todos os alunos registados na base de dados.

## Requisitos

- Python 3.x
- Biblioteca sqlite3 (inclusa no Python por padrão)
- Bibliotecas sys e os

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
