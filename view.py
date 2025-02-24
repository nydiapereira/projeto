import sqlite3

# Conexão com o banco de dados ou criar um novo banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Funcao para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) \
                VALUES (?,?,?,?,?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Funcao para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) \
                VALUES (?,?,?,?,?)", (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Funcao para exibir usuário
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Funcao para exibir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return livros

# Funcao para realizar empréstimo
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) \
                VALUES (?,?,?,?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Funcao para exibir todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, emprestimos.id, usuarios.sobrenome, \
                           emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Funcao para atualizar a data de devolucao de emprestimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

# Exemplos de uso das funcoes
# insert_book("Dom Quixote", "Miquel", "Editora 1", 1605, "123456")
# insert_user("Joao", "Silva", "Brasi", "joao@gmail.com", "+244 123")
# insert_loan(1, 1, "2022-08-20", None)

livros_emprestados = get_books_on_loan()
print(livros_emprestados)

# update_loan_return_date(2, "2022-09-21")
# exibir_livros()