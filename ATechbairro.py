import tkinter as tk
from tkinter import messagebox
import os
import sqlite3 

from dados import Cliente, GerenciadorClientes
VERSAO = "3.3.0"


CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "techbairro.db"
)
print(f"Banco em uso: {CAMINHO_BANCO}")

gerenciador = GerenciadorClientes(CAMINHO_BANCO)

id_em_edicao = None


janela = tk.Tk()

janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("480x460")
janela.resizable(False, False)

cabecalho = tk.Frame(
    janela,
    bg="#2c3e50"
)

cabecalho.pack(
    side="top",
    fill="x"
)

tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12,
).pack()

form = tk.Frame(janela)

form.pack(
    pady=20
)

campos = [
    "Nome",
    "Telefone",
    "E-mail",
    "Endereço"
]

entradas = {}

for i, campo in enumerate(campos):

    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )

    entrada = tk.Entry(
        form,
        width=30
    )

    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )

    entradas[campo] = entrada

status = tk.Label(
    janela,
    text="Sistema iniciado",
    fg="gray"
)

status.pack(
    pady=(0, 5)
)

contador = tk.Label(
    janela,
    text=""
)

contador.pack()


def atualizar_contador():

    total = gerenciador.total()

    contador.config(
        text=f"Clientes cadastrados: {total}"
    )

def limpar_campos():

    global id_em_edicao

    for entrada in entradas.values():

        entrada.delete(
            0,
            tk.END
        )

    id_em_edicao = None

    botao_salvar.config(text="Salvar")

def email_parece_valido(email):

    if "@" not in email:
        return False

    usuario, _, dominio = email.partition("@")

    if usuario == "":
        return False

    if "." not in dominio:
        return False

    return True

def salvar():

    global id_em_edicao

    nome = entradas["Nome"].get().strip()
    telefone = entradas["Telefone"].get().strip()
    email = entradas["E-mail"].get().strip()
    endereco = entradas["Endereço"].get().strip()

    if nome == "" or telefone == "" or email == "" or endereco == "":

        status.config(
            text="Preencha todos os campos.",
            fg="red"
        )

        return

    if not telefone.isdigit():

        status.config(
            text="Telefone inválido. Use somente números.",
            fg="red"
        )

        return

    if not email_parece_valido(email):

        status.config(
            text="E-mail inválido.",
            fg="red"
        )

        return

    cliente = Cliente(
        nome,
        telefone,
        email,
        endereco
    )

    try:

        if id_em_edicao is None:

            gerenciador.adicionar(cliente)

            status.config(
                text=f"Cliente '{nome}' cadastrado com sucesso!",
                fg="green"
            )

        else:

            alterou = gerenciador.atualizar(
                id_em_edicao,
                cliente
            )

            if not alterou:

                status.config(
                    text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                    fg="red"
                )

                limpar_campos()

                return

            status.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green"
            )

    except Exception as erro:

        status.config(
            text=f"Erro ao salvar: {erro}",
            fg="red"
        )

        return

    atualizar_contador()

    limpar_campos()

def cancelar():

    estava_editando = id_em_edicao is not None

    # Limpa os campos
    limpar_campos()

    if estava_editando:

        status.config(
            text="Edição cancelada. Nada foi alterado.",
            fg="gray"
        )

    else:

        status.config(
            text="Formulário limpo",
            fg="gray"
        )

def abrir_consulta():
    """
    Abre uma nova janela para consultar os clientes cadastrados.

    A janela possui uma Listbox que mostra todos os clientes
    armazenados no banco de dados.
    """

    consulta = tk.Toplevel(janela)

    consulta.title("Consulta de Clientes")
    consulta.geometry("600x400")
    consulta.resizable(False, False)

    tk.Label(
        consulta,
        text="Clientes cadastrados",
        font=("Arial", 14, "bold")
    ).pack(
        pady=10
    )

    lista = tk.Listbox(
        consulta,
        width=85,
        height=14
    )

    lista.pack(
        padx=10,
        pady=5
    )

    clientes_na_tela = []

    def atualizar_lista():

        lista.delete(
            0,
            tk.END
        )

        clientes_na_tela.clear()

        try:

            clientes = gerenciador.listar()

        except Exception as erro:

            lista.insert(
                tk.END,
                f"Erro ao consultar: {erro}"
            )

            return

        if len(clientes) == 0:

            lista.insert(
                tk.END,
                "Nenhum cliente cadastrado"
            )

            return

        for cliente in clientes:

            lista.insert(
                tk.END,
                cliente.resumo()
            )

            clientes_na_tela.append(cliente)

    def cliente_selecionado(acao):

        selecionado = lista.curselection()

        if not selecionado or selecionado[0] >= len(clientes_na_tela):

            messagebox.showwarning(
                "Atenção",
                f"Selecione um cliente antes de {acao}."
            )

            return None

        return clientes_na_tela[selecionado[0]]

    def editar_cliente():

        global id_em_edicao

        cliente = cliente_selecionado("editar")

        if cliente is None:

            return

        id_em_edicao = cliente.id

        entradas["Nome"].delete(
            0,
            tk.END
        )

        entradas["Nome"].insert(
            0,
            cliente.nome
        )

        entradas["Telefone"].delete(
            0,
            tk.END
        )

        entradas["Telefone"].insert(
            0,
            cliente.telefone
        )

        entradas["E-mail"].delete(
            0,
            tk.END
        )

        entradas["E-mail"].insert(
            0,
            cliente.email
        )

        entradas["Endereço"].delete(
            0,
            tk.END
        )

        entradas["Endereço"].insert(
            0,
            cliente.endereco
        )

        status.config(
            text=f"Editando cliente: {cliente.nome}",
            fg="blue"
        )

        botao_salvar.config(text="Salvar edição")

        consulta.destroy()

    def excluir_cliente():

        cliente = cliente_selecionado("excluir")

        if cliente is None:

            return

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja excluir o cliente {cliente.nome}?"
        )

        if confirmar:

            try:

                removeu = gerenciador.remover(
                    cliente.id
                )

            except sqlite3.Error as erro:

                messagebox.showerror(
                    "Erro no banco",
                    f"Não foi possível excluir o cliente.\n{erro}"
                )

                return

            if not removeu:

                messagebox.showwarning(
                    "Cliente não encontrado",
                    f"{cliente.nome} já não está mais no banco.\n"
                    f"A lista será atualizada."
                )

                atualizar_lista() 

                return

            atualizar_lista()

            atualizar_contador()

            status.config(
                text=f"Cliente '{cliente.nome}' excluído com sucesso!",
                fg="green"
            )

    botoes_consulta = tk.Frame(
        consulta
    )

    botoes_consulta.pack(
        pady=10
    )

    tk.Button(
        botoes_consulta,
        text="Editar selecionado",
        width=18,
        command=editar_cliente
    ).grid(
        row=0,
        column=0,
        padx=5
    )

    tk.Button(
        botoes_consulta,
        text="Excluir selecionado",
        width=18,
        command=excluir_cliente
    ).grid(
        row=0,
        column=1,
        padx=5
    )

    lista.bind(
        "<Double-Button-1>",
        lambda evento: editar_cliente()
    )

    atualizar_lista()

botoes = tk.Frame(
    janela
)

botoes.pack(
    pady=10
)

# Botão Salvar
#
# MUDOU NA AULA 20: o botão fica guardado na variável botao_salvar,
# para que o texto dele possa mudar no modo de edição.
# (o grid fica numa linha separada; se ficasse junto,
# a variável guardaria None em vez do botão)
botao_salvar = tk.Button(
    botoes,
    text="Salvar",
    width=13,
    command=salvar
)

botao_salvar.grid(
    row=0,
    column=0,
    padx=5
)

tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)

tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(
    row=0,
    column=2,
    padx=5
)

tk.Label(
    janela,
    text=f"v{VERSAO}",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)

atualizar_contador()

janela.mainloop()