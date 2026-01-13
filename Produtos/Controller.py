from DAO import ProdutoDAO
from Models import Produto

class ProdutosController:
    @classmethod
    def salvar_produto(cls, id:int, nome: str, preco:float, fornecedor: str, categoria: str):
        produto = Produto(id= id, nome= nome, preco= preco, fornecedor= fornecedor, categoria= categoria)
        ProdutoDAO.salvar_produto(produto)