import sqlite3


class Cliente:

    def __init__(self, nome, telefone, email, endereco, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"


class GerenciadorClientes:

    def __init__(self, caminho_banco):
        self.caminho_banco = caminho_banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):

        conexao = self.conectar()

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL,
                endereco TEXT NOT NULL
            )
        """)

        conexao.commit()
        conexao.close()

    def adicionar(self, cliente):

        conexao = self.conectar()

        cursor = conexao.execute("""
            INSERT INTO clientes
            (nome, telefone, email, endereco)
            VALUES (?, ?, ?, ?)
        """, (
            cliente.nome,
            cliente.telefone,
            cliente.email,
            cliente.endereco
        ))

        conexao.commit()

        cliente.id = cursor.lastrowid

        conexao.close()

    def listar(self):

        conexao = self.conectar()

        linhas = conexao.execute("""
            SELECT id, nome, telefone, email, endereco
            FROM clientes
            ORDER BY id
        """).fetchall()

        conexao.close()

        clientes = []

        for linha in linhas:

            cliente = Cliente(
                linha[1],
                linha[2],
                linha[3],
                linha[4],
                linha[0]
            )

            clientes.append(cliente)

        return clientes

    def total(self):

        conexao = self.conectar()

        quantidade = conexao.execute("""
            SELECT COUNT(*)
            FROM clientes
        """).fetchone()[0]

        conexao.close()

        return quantidade

    def atualizar(self, id_cliente, cliente):

        conexao = self.conectar()

        cursor = conexao.execute("""
            UPDATE clientes
            SET nome = ?,
                telefone = ?,
                email = ?,
                endereco = ?
            WHERE id = ?
        """, (
            cliente.nome,
            cliente.telefone,
            cliente.email,
            cliente.endereco,
            id_cliente
        ))

        conexao.commit()
        conexao.close()

        return cursor.rowcount == 1

    def remover(self, id_cliente):

        conexao = self.conectar()

        cursor = conexao.execute("""
            DELETE FROM clientes
            WHERE id = ?
        """, (id_cliente,))

        conexao.commit()
        conexao.close()

        return cursor.rowcount == 1