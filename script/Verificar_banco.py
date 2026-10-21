import sqlite3
import os


CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "techbairro.db"
)

print(f"Banco em uso: {CAMINHO_BANCO}")


clientes = [
    {
        "nome": "João Silva",
        "telefone": "61999999999",
        "email": "joao@gmail.com",
        "endereco": "Brasília"
    },
    {
        "nome": "Maria Souza",
        "telefone": "61988888888",
        "email": "maria@gmail.com",
        "endereco": "Ceilândia"
    },
    {
        "nome": "Pedro Santos",
        "telefone": "61977777777",
        "email": "pedro@gmail.com",
        "endereco": "Taguatinga"
    },
    {
        "nome": "Ana Oliveira",
        "telefone": "61966666666",
        "email": "ana@gmail.com",
        "endereco": "Samambaia"
    },
    {
        "nome": "Lucas Costa",
        "telefone": "61955555555",
        "email": "lucas@gmail.com",
        "endereco": "Guará"
    },
    {
        "nome": "Mariana Alves",
        "telefone": "61944444444",
        "email": "mariana@gmail.com",
        "endereco": "Águas Claras"
    },
    {
        "nome": "Carlos Pereira",
        "telefone": "61933333333",
        "email": "carlos@gmail.com",
        "endereco": "Sobradinho"
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