from Clientes.DAO import PessoaDAO
from Clientes.Models import Pessoa
import re

class ClientesController:
    @classmethod
    def valida_se_o_email_e_valido(cls, email:str) -> bool:
        validacao_da_string = re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com')
        validacao_email_valido = re.fullmatch(validacao_da_string, email)
        if validacao_email_valido != None:
            return True
        else:
            print("Insira um email valido.")
            return False

    @classmethod
    def valida_se_o_cpf_e_valido(cls, cpf:str) -> bool:
        validacao_da_string = re.compile('[0-9]{11}')
        validacao_email_valido = re.fullmatch(validacao_da_string, cpf)
        if validacao_email_valido != None:
            return True
        else:
            print("Insira um CPF valido e que contenha 11 digitos")
            return False


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
    def verifica_veracidade_dos_dados_inseridos(cls, nome: str, cpf:str, email:str):
        validacao_email = cls.valida_se_o_email_e_valido(email)
        validacao_cpf = cls.valida_se_o_cpf_e_valido(cpf)
        if len(nome)>=8 and validacao_email==True and validacao_cpf==True:
            return True
        elif len(nome)<8:
            print("Nome contem menos de 8 digitos. Insira um nome com mais de oito digitos. \n entrou no len(nome)")
            return False
        else:
            print('entrou no else sem condicoess. se o valida_email ou o cpf forem false, ele vem pra ca')
            return False

    @classmethod
    def salvar_cliente(cls, nome: str, cpf:str, email:str):
        id_pessoa = PessoaDAO.ler_todas_as_pessoas()
        id_pessoa = id_pessoa[1] + 1
        tipo_pessoa = {1 : "Cliente"}
        verificacao_dos_dados_inseridos = cls.verifica_veracidade_dos_dados_inseridos(nome= nome, cpf= cpf, email= email)
        if verificacao_dos_dados_inseridos:
            pessoa = Pessoa(id = id_pessoa, nome = nome,  cpf= cpf, email= email, tipo_pessoa= tipo_pessoa)
            return PessoaDAO.salvar_pessoa(pessoa)
        return False
    
    @classmethod
    def listar_todos_as_pessoas(cls):
        pessoas, _ = PessoaDAO.ler_todas_as_pessoas()
        return pessoas
    
    @classmethod
    def alterar_pessoa_existente(cls, id : int, nome: str, cpf:str, email:str):
        cls.listar_todos_as_pessoas()
        verifica_dados = cls.verifica_veracidade_dos_dados_inseridos(nome =nome, cpf= cpf, email= email)
        existe_pessoa, pessoa, pessoas = PessoaDAO.buscar_pessoa(id= id)
        print(f'Existe pessoa {existe_pessoa}')
        print(f' Verifica dados {verifica_dados}')
        if verifica_dados is False:
            print(f'dentro do if {verifica_dados}')
            return False, existe_pessoa
        else:
            _ = PessoaDAO.atualizar_pessoa(id= id, nome= nome, cpf= cpf, email= email)
            print(f'etdgaduy {_}')
            return True, True
        if _ is False:
            return False
        return True

    @classmethod
    def excluir_pessoa(cls, id: int):
        pessoa_excluida = PessoaDAO.excluir_pessoa(id = id)
        if pessoa_excluida:
            return True
        return False
    