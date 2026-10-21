import sqlite3
import os


CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "techbairro.db"
)

print(f"Banco em uso: {CAMINHO_BANCO}")


conexao = sqlite3.connect(CAMINHO_BANCO)

conexao.execute("BEGIN EXCLUSIVE")

print("Banco travado.")
print("Pressione Enter para liberar o banco.")

input()

conexao.rollback()
conexao.close()

print("Banco liberado.")