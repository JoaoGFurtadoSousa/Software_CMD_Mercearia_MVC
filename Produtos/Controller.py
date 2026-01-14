from DAO import ProdutoDAO
from Models import Produto

class ProdutosController:
    @classmethod
    def salvar_produto(cls, nome: str, preco:float, fornecedor: str, categoria: str):
        id_produto = ProdutoDAO.ler_todos_os_produtos()
        id_produto = id_produto[1] + 1
        produto = Produto(id = id_produto, nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
        return ProdutoDAO.salvar_produto(produto)
   
    @classmethod
    def listar_todos_os_produtos(cls):
        produtos, _ = ProdutoDAO.ler_todos_os_produtos()
        return produtos
    
    @classmethod
    def alterar_produto_existente(cls, id : int, nome: str, preco:float, fornecedor: str, categoria: str):
        _, produto = ProdutoDAO.buscar_produto(id)
        print(produto)
