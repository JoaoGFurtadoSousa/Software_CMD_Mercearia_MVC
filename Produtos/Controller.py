from Produtos.DAO import ProdutoDAO
from Produtos.Models import Produto

class ProdutosController:
    @classmethod
    def verifica_se_ha_campos_nulos(cls, **kwargs):
        print(kwargs)
        for chave, valor in kwargs.items():
            if valor is None: #anotas o is
                return False
            
            if isinstance(valor, str) and not valor.strip(): #anotar isinstance e strip()
                return False
        return True
            

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
        cls.listar_todos_os_produtos()
        _= ProdutoDAO.atualizar_produto(id= id,
                                        nome= nome,
                                        preco= preco, 
                                        fornecedor= fornecedor,
                                        categoria= categoria)
        if _ is False:
            return False
        """print(produto)
        print(produtos)"""

    @classmethod
    def excluir_produto(cls, id: int):
        produto_excluido = ProdutoDAO.excluir_produto(id = id)
        if produto_excluido:
            return True
        return False
    
   
