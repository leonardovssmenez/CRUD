import unittest

class TestAdicionarProduto(unittest.TestCase):

    def test_fluxo_principal(self):
        # Simulando o clique em "adicionar produto"
        # e a exibição da tela de cadastro
        
        # Preenchendo as informações do produto
        produto = {
            'nome': 'Produto Teste',
            'preco': 10.99,
            'descricao': 'Descrição do produto teste'
        }
        
        # Simulando o clique em "registrar produto"
        resultado = registrar_produto(produto)
        
        # Verificando se a mensagem de sucesso é exibida
        self.assertEqual(resultado, 'Produto cadastrado')
        
    def test_fluxo_alternativo_1(self):
        # Simulando o clique em "adicionar produto"
        # e a exibição da tela de cadastro
        
        # Não preenchendo os campos necessários
        
        # Simulando o clique em "registrar produto"
        resultado = registrar_produto({})
        
        # Verificando se a mensagem de erro é exibida
        self.assertEqual(resultado, 'Informações insuficientes')
        
    def test_fluxo_alternativo_2(self):
        # Simulando o clique em "adicionar produto"
        # e a exibição da tela de cadastro
        
        # Preenchendo as informações do produto
        produto = {
            'nome': 'Produto Teste',
            'preco': 10.99,
            'descricao': 'Descrição do produto teste'
        }
        
        # Simulando o clique em "registrar produto"
        resultado = registrar_produto(produto)
        
        # Verificando se a mensagem de erro é exibida
        self.assertEqual(resultado, 'Produto já cadastrado')

# Função fictícia para registrar o produto
def registrar_produto(produto):
    if not produto:
        return 'Informações insuficientes'
    elif produto_ja_cadastrado(produto):
        return 'Produto já cadastrado'
    else:
        return 'Produto cadastrado'

# Função fictícia para verificar se o produto já está cadastrado
def produto_ja_cadastrado(produto):
    # Implementação fictícia
    produtos_cadastrados = ['Produto1', 'Produto2', 'Produto3']
    if produto['nome'] in produtos_cadastrados:
        return True
    else:
        return False

if __name__ == '__main__':
    unittest.main()
