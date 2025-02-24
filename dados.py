import sqlite3

def create_tables():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    # Criação da tabela livros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            editora TEXT,
            ano_publicacao INTEGER,
            isbn TEXT UNIQUE
        )
    ''')

    # Criação da tabela usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            endereco TEXT,
            email TEXT UNIQUE,
            telefone TEXT
        )
    ''')

    # Criação da tabela emprestimos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_livro INTEGER NOT NULL,
            id_usuario INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao TEXT,
            FOREIGN KEY (id_livro) REFERENCES livros(id),
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
    ''')

    conn.commit()
    conn.close()

# Cria as tabelas antes de executar o restante do código
create_tables()

# Resto do seu código (inserir livros, usuários, empréstimos, etc.)
# ...