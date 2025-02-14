import sqlite3
import hashlib

def hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

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

    senha_hash = hash(senha)
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha_hash))

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

def deletar_usuario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

def deletar_todos_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='usuarios'")  # Reseta o ID
    conexao.commit()
    conexao.close()
    print("Todos os usuários foram removidos e o ID foi resetado.")
