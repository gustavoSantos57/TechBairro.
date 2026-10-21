import tkinter as tk
from tkinter import messagebox
import os

from dados import Cliente, GerenciadorClientes
# NOVO NA AULA 18: a versão fica num único lugar.
# Para publicar uma versão nova, basta mudar aqui
# (e registrar a mudança no CHANGELOG).
VERSAO = "3.2.1"


CAMINHO_BANCO = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "techbairro.db"
)

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

            gerenciador.atualizar(
                id_em_edicao,
                cliente
            )

            status.config(
                text=f"Cliente '{nome}' atualizado com sucesso!",
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

    limpar_campos()

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

    def atualizar_lista():

        lista.delete(
            0,
            tk.END
        )


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

    def editar_cliente():

        global id_em_edicao


        selecionado = lista.curselection()


        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente."
            )

            return


        indice = selecionado[0]

        clientes = gerenciador.listar()


        if indice >= len(clientes):

            return


        cliente = clientes[indice]

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


        consulta.destroy()

    def excluir_cliente():

        selecionado = lista.curselection()


        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente."
            )

            return


        indice = selecionado[0]

        clientes = gerenciador.listar()


        if indice >= len(clientes):

            return


        cliente = clientes[indice]


        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja excluir o cliente {cliente.nome}?"
        )


        if not confirmar:

            return


        gerenciador.remover(
            cliente.id
        )


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


    atualizar_lista()

botoes = tk.Frame(
    janela
)

botoes.pack(
    pady=10
)


tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(
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