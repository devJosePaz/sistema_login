import sqlite3

banco = sqlite3.connect('database.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL, senha TEXT NOT NULL)")

#cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'adminpass')")

#cursor.execute("DELETE FROM usuarios WHERE id IN (2,3,4)")

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Exibir os dados formatados
print("ID | Usuário  | Senha")
print("-" * 30)

for usuario in usuarios:
    print(f"{usuario[0]:<2} | {usuario[1]:<8} | {usuario[2]}")

banco.commit()
banco.close()
