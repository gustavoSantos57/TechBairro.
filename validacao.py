# ===========================================================
# VALIDAÇÃO (Aula 21)
# ===========================================================
#
# Responsabilidade: as regras de negócio do cadastro (RF01 a RF03).
# Este arquivo não sabe nada de janela nem de banco.

# Classe responsável por conferir se um cliente pode ser gravado
class ValidadorCliente:

    # Confere todas as regras do cliente.
    #
    # Retorna a mensagem do primeiro problema encontrado,
    # ou None se o cliente estiver válido.
    def validar(self, cliente):

        # RF01: todos os campos são obrigatórios
        vazios = []

        if cliente.nome == "":
            vazios.append("Nome")

        if cliente.telefone == "":
            vazios.append("Telefone")

        if cliente.email == "":
            vazios.append("E-mail")

        if cliente.endereco == "":
            vazios.append("Endereço")

        # Se houver algum campo vazio
        # (mensagem idêntica à do salvar() da versão 3.3.0)
        if vazios:
            return "Preencha todos os campos."

        # RF02: o telefone precisa ter somente números
        if not cliente.telefone.isdigit():
            return "Telefone inválido. Use somente números."

        # RF03: o e-mail precisa estar no formato nome@dominio.com
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido."

        # Nenhum problema encontrado
        return None

    # MUDOU NA AULA 21: era uma função solta no techbairro.py,
    # agora é um método do ValidadorCliente
    def email_parece_valido(self, email):

        if "@" not in email:
            return False

        usuario, _, dominio = email.partition("@")

        if usuario == "":
            return False

        if "." not in dominio:
            return False

        return True
