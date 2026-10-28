changelog da techbairro
## v3.3.2 (Aula 27)
### Adicionado
- README com requisitos, instalação e configuração do banco.
- Arquivo requirements.txt.
- Manual de uso em docs/manual_de_uso.md.
- Registro de testes em docs/registro_de_testes.md.
## v3.2.1 (Aula 18)
### Alterado
- O número da versão passou a ficar 3.2.1.
### Adicionado
- Script scripts/gerar_pacote.py, que reúne os arquivos do projeto e gera o pacote da versão (TechBairro-3.2.1.zip), deixando de fora o banco de dados e os arquivos gerados pelo Python.
- Arquivo COMO_EXECUTAR.txt, com os requisitos e o passo a passo para rodar o programa num computador novo.
## v3.2.0 (aula 16)
### alterado
- O banco agora é aberto pelo caminho completo (os.path + file), sempre na pasta do projeto, não importa de onde o programa seja executado.
## adicionado
- Mensagem "banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.
## v3.1.0 (aula 15)
### corrigido
- Corrigido: o método atualizar() fazia mudanças mas não executava o commit() corretamente.
- Corrigido: edição e exclusão passaram a usar o id do banco (evita remoção/edição por índice inválido).
- Corrigido: validação de telefone (agora rejeita caracteres não numéricos).
- Corrigido: casos de endereço vazio que levantavam exceptions foram tratados.
- Corrigido: ordenação e contagem exibida na tela agora coincidem com os resultados do banco.
## v3.0.0 (aula 14)
### alterado
- O gerenciadorclientes deixou de guardar os clientes numa lista em memória e passou a gravar no banco sqlite techbairro.db.
- A tela foi atualizada para usar ids do banco em vez de índices de lista.
- Operações crud (adicionar, listar, atualizar, remover) agora persistem no banco.
### adicionado
- Interface gráfica principal (cadastro) com formulário e botões de salvar, consultar e limpar.
## v2.0.0 (aulas 11 e 12)
### adicionado
- Implementação das classes de domínio e a tela de consulta com listagem e seleção de clientes.
- Antes da v2.0.0 (aulas 5 a 10)
- Protótipos de telas, eventos e validações básicas do formulário (campos obrigatórios, navegação entre campos).
