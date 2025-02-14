from db import criar_tabela, adicionar_usuario, listar_usuarios, deletar_usuario, deletar_todos_usuarios, hash

def menu():
    while True:
        print("\n=== GERENCIAMENTO DE USUÁRIOS ===")
        print("1 - Criar tabela")
        print("2 - Adicionar usuário")
        print("3 - Listar usuários")
        print("4 - Deletar usuário")
        print("5 - Deletar todos os usuários")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tabela()
            print("Tabela criada (se não existir).")
        elif opcao == "2":
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            adicionar_usuario(usuario, hash(senha))
            print("Usuário adicionado com sucesso!")
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            id_usuario = input("Digite o ID do usuário a ser deletado: ")
            if id_usuario.isdigit():
                deletar_usuario(int(id_usuario))
                print("Usuário deletado!")
            else:
                print("ID inválido. Digite um número.")
        elif opcao =="5":
             deletar_todos_usuarios()

        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
