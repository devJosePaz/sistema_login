import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect('database.db')

# Função para criar a tabela (caso não exista)
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

# Função para adicionar usuário
def adicionar_usuario(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
    conexao.commit()
    conexao.close()

# Função para listar todos os usuários cadastrados
def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()

    # Exibir os dados formatados
    print("ID | Usuário  | Senha")
    print("-" * 30)
    for usuario in usuarios:
        print(f"{usuario[0]:<2} | {usuario[1]:<8} | {usuario[2]}")
