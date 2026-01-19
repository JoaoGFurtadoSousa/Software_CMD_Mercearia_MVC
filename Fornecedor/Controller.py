from Fornecedor.DAO import FornecedorDAO
from Fornecedor.Models import Fornecedor

class FornecedoresController:
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
    def salvar_fornecedor(cls, nome: str):
        id_fornecedor = FornecedorDAO.ler_todas_os_fornecedores()
        id_fornecedor = id_fornecedor[1] + 1
        fornecedor = Fornecedor(id = id_fornecedor, nome = nome)
        return FornecedorDAO.salvar_fornecedor(fornecedor)
   
    @classmethod
    def listar_todos_os_fornecedores(cls):
        fornecedores, _ = FornecedorDAO.ler_todas_os_fornecedores()
        return fornecedores
    
    @classmethod
    def alterar_fornecedor_existente(cls, id : int, nome: str):
        cls.listar_todos_os_fornecedores()
        _ = FornecedorDAO.atualizar_fornecedor(id= id, nome= nome)
        if _ is False:
            return False
        return True

    @classmethod
    def excluir_fornecedor(cls, id: int):
        fornecedor_excluido = FornecedorDAO.excluir_fornecedor(id = id)
        print(f'Fornecdor controller{fornecedor_excluido}')
        if fornecedor_excluido:
            return True
        return False
    
   
