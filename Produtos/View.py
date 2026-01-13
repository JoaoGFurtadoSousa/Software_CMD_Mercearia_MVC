from Controller import ProdutosController

controller = ProdutosController()
produto = controller.salvar_produto(id=5, nome= "Nintendo Switch", preco=2.500, fornecedor= "Nintendo", categoria= "Videogames")

if produto:
    print(produto)
else:
    print('Erro ao criar o produto')
