# TechBairro — Cadastro de Cliente

Sistema simples de cadastro de clientes feito em Python, com janelas em Tkinter e banco de dados SQLite. Versão atual: **v3.2**.

## O que o sistema faz

Permite cadastrar, consultar, editar e excluir clientes. Cada cliente tem nome, telefone, e-mail e endereço. Os dados ficam salvos no arquivo `techbairro.db`, então continuam lá mesmo depois de fechar o programa. A tela principal mostra quantos clientes estão cadastrados.

O sistema valida os dados antes de salvar: todos os campos são obrigatórios, o telefone só pode ter números e o e-mail precisa ter algo antes do @ e um ponto depois dele.

## Como rodar

Você precisa do Python 3 instalado (o Tkinter já vem junto na instalação padrão). Abra um terminal na pasta do projeto e rode:

    python techbairro.py

O terminal mostra a mensagem "Banco em uso" com o caminho do banco, e a janela de cadastro abre. O botão **Consultar** abre a lista de clientes, onde dá para editar ou excluir o cliente selecionado.

## Estrutura do projeto

    TechBairro/
    ├── techbairro.py      programa principal (telas e eventos)
    ├── Dados.py           classes Cliente e GerenciadorClientes (acesso ao banco)
    ├── techbairro.db      banco de dados local (não entra no versionamento)
    ├── CHANGELOG.md       histórico das versões
    ├── README.md          este arquivo
    ├── scripts/           scripts de apoio
    └── docs/              documentação (modelagem do banco, testes e verificação)

O `Dados.py` precisa ficar na mesma pasta do `techbairro.py`, porque o programa importa as classes dele.

## Scripts de apoio

Ficam na pasta `scripts/` e usam o mesmo `techbairro.db` da pasta principal.

- `importar_planilha_antiga.py`: importa os clientes da planilha antiga para o banco. Rode só uma vez, senão os clientes ficam duplicados.
- `verificar_banco.py`: confere o banco e mostra o "Banco verificado" com o caminho e o total de clientes.
- `travar_banco.py`: trava o banco de propósito, para testar o que acontece quando ele está ocupado. Aperte Enter para liberar.

## Versões

O histórico completo de cada versão está no arquivo [CHANGELOG.md](CHANGELOG.md). O projeto segue a ideia de versionamento semântico (MAJOR.MINOR.PATCH).

## Observações

O arquivo `techbairro.db` tem dados reais de clientes, por isso não deve ser enviado para o Git nem compartilhado fora da equipe.