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
            'nome': 'Produto Teste 1',
            'preco': 10.99,
            'descricao': 'Descrição do produto teste'
        }
        
        # Simulando o clique em "registrar produto"
        resultado = registrar_produto(produto)
        
        # Verificando se a mensagem de erro é exibida
        self.assertEqual(resultado, 'Produto já cadastrado')

if __name__ == '__main__':
    unittest.main()
