sistema-de-cadastro-usuarios/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── crud.py
│
├── tests/
│   └── test_crud.py
│
├── .gitignore
├── requirements.txt
└── README.md

📁 app/database.py
import sqlite3

DB_NAME = "usuarios.db"


def get_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    return sqlite3.connect(DB_NAME)


def create_tables():
    """Cria as tabelas necessárias no banco."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        conn.commit()

        📁 app/models.py
        class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

        📁 app/crud.py
        from app.database import get_connection
from app.models import Usuario


def criar_usuario(usuario: Usuario):
    """Insere um novo usuário no banco."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
            (usuario.nome, usuario.email)
        )
        conn.commit()


def listar_usuarios():
    """Retorna todos os usuários cadastrados."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        return cursor.fetchall()


def atualizar_usuario(usuario_id: int, nome: str, email: str):
    """Atualiza um usuário existente."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
            (nome, email, usuario_id)
        )
        conn.commit()


def deletar_usuario(usuario_id: int):
    """Remove um usuário pelo ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        conn.commit()

📁 app/main.py
from app.database import create_tables
from app.models import Usuario
from app.crud import (
    criar_usuario,
    listar_usuarios,
    atualizar_usuario,
    deletar_usuario
)


def menu():
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    create_tables()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            usuario = Usuario(nome, email)
            criar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            usuarios = listar_usuarios()
            for u in usuarios:
                print(u)

        elif opcao == "3":
            usuario_id = int(input("ID do usuário: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            atualizar_usuario(usuario_id, nome, email)
            print("Usuário atualizado!")

        elif opcao == "4":
            usuario_id = int(input("ID do usuário: "))
            deletar_usuario(usuario_id)
            print("Usuário removido!")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

📁 tests/test_crud.py
def test_exemplo():
    assert 1 + 1 == 2

📄 requirements.txt

📄 .gitignore
__pycache__/
*.db
.env

📄 README.md
# Sistema de Cadastro de Usuários

Projeto em Python que implementa um sistema de cadastro de usuários com operações CRUD,
utilizando banco de dados SQLite. Desenvolvido para fins de estudo e portfólio.

## 🚀 Tecnologias Utilizadas
- Python 3
- SQLite

## 📂 Estrutura do Projeto

sistema-de-cadastro-usuarios/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── crud.py
│
├── tests/
│   └── test_crud.py
│
├── .gitignore
├── requirements.txt
└── README.md

## ▶️ Como Executar

```bash
git clone https://github.com/Orneles/sistema-de-cadastro-usuarios.git
cd sistema-de-cadastro-usuarios
python app/main.py



