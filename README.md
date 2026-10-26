# TechBairro

Sistema desktop para cadastro e gerenciamento de clientes da associação de moradores, desenvolvido em Python com uma interface gráfica simples e um banco de dados local.

**Versão atual:** 3.3.2 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar, editar e excluir clientes cadastrados.
- Armazenar os dados em um banco de dados local SQLite.
- Exibir a quantidade de clientes cadastrados.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows, Linux ou macOS, com Python e Tkinter disponíveis |
| Python | Python 3 instalado (versão testada: preencher após conferir) |
| Tkinter | Necessário para abrir a interface gráfica |
| Bibliotecas externas | Nenhuma |
| Internet | Necessária para baixar o projeto; não é necessária para o uso normal |

## Instalação

### Opção 1 — Baixar usando Git

1. Instale o Python e o Git, caso ainda não estejam instalados.
2. Abra o terminal e execute:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

3. Entre na pasta do projeto:

```bash
cd techbairro
```

4. Execute o programa:

```bash
python techbairro.py
```

### Opção 2 — Baixar pelo GitHub

1. Acesse o repositório da TechBairro no GitHub.
2. Clique em **Code** e depois em **Download ZIP**.
3. Extraia o arquivo ZIP para uma pasta do computador.
4. Abra o terminal dentro da pasta extraída.
5. Execute:

```bash
python techbairro.py
```

### Dependências

A TechBairro utiliza módulos da biblioteca padrão do Python e não precisa instalar pacotes externos.

O arquivo `requirements.txt` registra essa informação. Para conferir se ele pode ser processado pelo pip, execute:

```bash
python -m pip install -r requirements.txt
```

Após a execução, a janela principal da TechBairro deverá abrir. No terminal, também deverá aparecer a mensagem `Banco em uso:`, seguida do caminho do arquivo de banco de dados utilizado pelo programa.

Se o comando `python` não funcionar no Windows, tente utilizar `py` no lugar dele.

## Configuração do banco de dados

A TechBairro utiliza o SQLite para armazenar os clientes cadastrados. O arquivo do banco de dados é chamado `techbairro.db` e fica na mesma pasta do projeto, conforme a configuração do programa.

O banco é criado automaticamente quando o sistema precisa abrir ou inicializar a base de dados. A mensagem `Banco em uso:` exibida no terminal informa o caminho do banco que está sendo utilizado.

O arquivo `techbairro.db` não deve ser enviado ao GitHub, pois pode conter informações pessoais dos clientes. Para evitar o envio acidental, ele deve ser incluído no arquivo `.gitignore`.

Para fazer uma cópia de segurança, feche a TechBairro e copie o arquivo `techbairro.db` para uma pasta protegida. Guarde essa cópia em um local seguro e evite compartilhá-la, pois ela pode conter dados pessoais.

## Como usar

O passo a passo para cadastrar, consultar, editar e excluir clientes está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

| Arquivo ou pasta | Descrição |
|---|---|
| `techbairro.py` | Arquivo principal que inicia o programa e apresenta a interface gráfica. |
| `dados.py` | Contém as classes responsáveis pelo gerenciamento dos clientes e dos dados. |
| `techbairro.db` | Banco de dados local que armazena os clientes cadastrados; não deve ser enviado ao GitHub. |
| `requirements.txt` | Informa que o projeto não possui dependências externas. |
| `CHANGELOG.md` | Registra as alterações realizadas nas versões do projeto. |
| `docs/manual_de_uso.md` | Contém as instruções para utilizar o sistema. |
| `.gitignore` | Define os arquivos e pastas que não devem ser enviados ao repositório. |

## Autor

**Gustavo dos Santos Pereira**  
Curso Técnico em Desenvolvimento de Sistemas  
Senac DF
