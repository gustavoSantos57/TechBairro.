import sqlite3
import os


CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "techbairro.db"
)

print(f"Banco em uso: {CAMINHO_BANCO}")

clientes = [
    {
        "nome": "Carlos Pereira",
        "telefone": "61988887777",
        "email": "carlos@email.com",
        "endereco": "Quadra 3 Casa 10"
    },
    {
        "nome": "Beatriz Lima",
        "telefone": "61977776666",
        "email": "bia@email.com",
        "endereco": "Rua 5 Casa 2"
    },
    {
        "nome": "Diego Martins",
        "telefone": "61966665555",
        "email": "diego@email",
        "endereco": "Rua 8 Casa 1"
    },
    {
        "nome": "Eduarda Rocha",
        "telefone": "61955554444",
        "email": "eduarda@email.com",
        "endereco": ""
    },
    {
        "nome": "Fábio Nunes",
        "telefone": "6194444ABCD",
        "email": "fabio@email.com",
        "endereco": "Rua 9 Casa 4"
    },
    {
        "nome": "Gabriela Souza",
        "telefone": "61988887777",
        "email": "gabi@email.com",
        "endereco": "Rua 2 Casa 7"
    },
    {
        "nome": "Helena Dias",
        "telefone": "61933332222",
        "email": "helena@email.com",
        "endereco": "Rua 7 Casa 3"
    }
]


conexao = sqlite3.connect(CAMINHO_BANCO)

conexao.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
""")


for cliente in clientes:

    conexao.execute("""
        INSERT INTO clientes
        (nome, telefone, email, endereco)
        VALUES (?, ?, ?, ?)
    """, (
        cliente["nome"],
        cliente["telefone"],
        cliente["email"],
        cliente["endereco"]
    ))


conexao.commit()
conexao.close()

print("Clientes importados com sucesso!")