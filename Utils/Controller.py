from Utils.DAO import PessoaDAO
from Utils.Models import Pessoa

class UtilsesController:
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
    def salvar_utils(cls, nome: str):
        id_pessoa = PessoaDAO.ler_todas_as_pessoas()
        id_pessoa = id_pessoa[1] + 1
        pessoa = Pessoa(id = id_pessoa, nome = nome)
        return PessoaDAO.salvar_pessoa(pessoa)
   
    @classmethod
    def listar_todos_as_pessoas(cls):
        pessoas, _ = PessoaDAO.ler_todas_as_pessoas()
        return pessoas
    
    @classmethod
    def alterar_pessoa_existente(cls, id : int, nome: str):
        cls.listar_todos_as_pessoas()
        _ = PessoaDAO.atualizar_pessoa(id= id, nome= nome)
        if _ is False:
            return False
        return True

    @classmethod
    def excluir_pessoa(cls, id: int):
        pessoa_excluida = PessoaDAO.excluir_pessoa(id = id)
        print(f'Fornecdor controller{pessoa_excluida}')
        if pessoa_excluida:
            return True
        return False
    
   
