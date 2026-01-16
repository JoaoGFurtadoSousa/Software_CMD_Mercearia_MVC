from Produtos.DAO import CategoriaDAO
from Produtos.Models import Categoria

class CategoriasController:
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
    def salvar_categoria(cls, nome: str, preco:float, fornecedor: str, categoria: str):
        id_categoria = CategoriaDAO.ler_todas_as_categorias()
        id_categoria = id_categoria[1] + 1
        categoria = Categoria(id = id_categoria, nome = nome)
        return CategoriaDAO.salvar_categoria(categoria)
   
    @classmethod
    def listar_todos_os_categorias(cls):
        categorias, _ = CategoriaDAO.ler_todas_as_categorias()
        return categorias
    
    @classmethod
    def alterar_categoria_existente(cls, id : int, nome: str):
        cls.listar_todos_os_categorias()
        _= CategoriaDAO.atualizar_categoria(id= id, nome= nome)
        if _ is False:
            return False

    @classmethod
    def excluir_categoria(cls, id: int):
        categoria_excluido = CategoriaDAO.excluir_categoria(id = id)
        if categoria_excluido:
            return True
        return False
    
   
