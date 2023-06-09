# CRUD

--> CASOS DE USO

1. ADICIONAR PRODUTO

- Objetivo: cadastrar um produto
- Atores: administrador

Fluxo principal:

- Administrador clica em "adicionar produto"
- Sistema mostra tela de cadastro com campos necessários para preenchimento
- Administrador preenche informações do produto
- Após preenchimento, adminsitrador clica em registrar produto, se problema encontrado seguir para Fluxo Alternativo.
- Sistema exibe mensagem "Produto cadastrado".

Fluxo alternativo 1:

- Administrador não preencheu os campos necessários e clicou em registrar produto
- Sistema exibe mensagem "Informações insuficientes" e exibe tela de cadastro novamente voltando para o Fluxo Principal.

Fluxo Alternativo 2:

- Administrador preenche os campos e clica em registrar produto, porém as informações são de um produto já existente.
- Sistema exibe mensagem "Produto já cadastrado".

2. ATUALIZAR PRODUTO

- Objetivo: atualizar o cadastro de um produto
- Atores: administrador

Fluxo principal:

- Administrador clica em "atualizar produto"
- Sistema mostra tela de pesquisa para o produto ser selecionado
- Administrador seleciona o produto que quer atualizar
- Sistema mostra tela de cadastro do produto
- Administrador modifica as informações desejadas
- Sistema exibem mensagem "Produto atualizado"

Fluxo Alternativo:

- Administrador não preencheu os campos necessários e clicou em atualizar produto
- Sistema exibe mensagem "Informações insuficientes" e exibe tela de cadastro novamente voltando para o Fluxo Principal.

3 DELETAR PRODUTO

- Objetivo: excluir um produto
- Atores: administrador

Fluxo principal:

- Administrador clica em "deletar produto"
- Sistema mostra tela de pesquisa para o produto ser selecionado
- Administrador seleciona o produto que quer deletar clica em excluir
- Sistema exibe mensagem "Produto excluido"

Fluxo Alternativo:

- Administrador pesquisa por produto inexistente
- Sistema exibe mensagem "Produto não foi encontrado" e exibe a tela de pesquisa novamente, retornando ao Fluxo Principal.

4 LISTAR PRODUTO

- Objetivo: mostrar um produto
- Atores: administrador

Fluxo principal:

- Administrador clica em "listar produto"
- Sistema mostra tela de pesquisa
- Administrador digita codigo do produto que deseja
- Sistema exibe todas as informações do produto

Fluxo Alternativo:

- Administrador pesquisa por produto inexistente
- Sistema exibe mensagem "Produto não foi encontrado" e exibe a tela de pesquisa novamente, retornando ao Fluxo Principal.

5 LISTAR TODOS OS PRODUTOS

- Objetivo: mostrar um produto
- Atores: administrador

Fluxo principal:

- Administrador clica em "listar todos produtos"
- Sistema exibe todos os produtos cadastrados

Fluxo Alternativo:

- Administrador clica em "listar todos produtos"
- Sistema não possui nenhum produto cadastrado, exibe mensagem "Nenhum produto cadastrado".
