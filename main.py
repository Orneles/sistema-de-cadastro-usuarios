from database import criar_tabela
from crud import adicionar_usuario, listar_usuarios, remover_usuario

def menu():
    print("\n=== Sistema de Cadastro ===")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Remover usuário")
    print("0 - Sair")

def main():
    criar_tabela()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionar_usuario(nome, email)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            usuarios = listar_usuarios()
            for u in usuarios:
                print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")

        elif opcao == "3":
            id_usuario = input("ID do usuário: ")
            remover_usuario(id_usuario)
            print("Usuário removido!")

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()


