import json
from Utils.Models import Pessoa
from pathlib import Path


BASE_DIR = Path(__file__).parent
ARQUIVO_PESSOAS = BASE_DIR / f"{BASE_DIR.name}.txt"


class PessoaDAO:
    @classmethod
    def ler_todas_as_pessoas(cls):
        pessoas = []
        ultimo_id = 0
        with open(ARQUIVO_PESSOAS, 'r', encoding='utf-8') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                pessoas.append(data_em_dict)
                for pessoa in pessoas:
                     ultimo_id = pessoa['id']
            return [pessoas, ultimo_id]


    @classmethod
    def salvar_pessoa(cls, pessoa: Pessoa):
            with open(ARQUIVO_PESSOAS, 'a') as escrever_no_arquivo:
                try:
                    pessoa = pessoa.exibir_todos_os_dados_da_instancia()
                    instancia_em_json = json.dumps(pessoa)
                    escrever_no_arquivo.writelines(f'{instancia_em_json}\n')
                    return True
                except:
                     return False


    @classmethod
    def buscar_pessoa(cls, id: int):
        pessoas = []
        pessoa_encontrada = None

        with open(ARQUIVO_PESSOAS, 'r', encoding='utf-8') as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue

                data = json.loads(linha)
                pessoas.append(data)

                if data['id'] == id:
                    pessoa_encontrada = data

        if pessoa_encontrada:
            return True, pessoa_encontrada, pessoas

        return False, None, pessoas

    @classmethod
    def excluir_pessoa(cls, id:int):
        pessoas = []
        existe_pessoa = True
        with open(ARQUIVO_PESSOAS, 'r') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos 
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                pessoas.append(data_em_dict)
                for pessoa in pessoas:
                    print(f'Fornecedor {pessoa}')
                    if pessoa["id"] == id:
                          pessoas.remove(pessoas)
                    else:
                        existe_pessoa = False                            
        with open(ARQUIVO_PESSOAS, 'w') as base_de_dados_das_pessoas:
                for pessoa in pessoas:         
                    pessoa_convertida_em_str = json.dumps(pessoa)
                    base_de_dados_das_pessoas.write(f'{pessoa_convertida_em_str}' + '\n')
                return True
  

    
 
    @classmethod
    def atualizar_pessoa(cls, id: int, nome: str):
         pessoas = []
         existe_pessoa, pessoa, pessoas = cls.buscar_pessoa(id= id)
         for pessoa in pessoas:
                    if pessoa["id"] == id:
                        pessoa["nome"] = nome
         with open(ARQUIVO_PESSOAS, 'w') as base_de_dados_das_pessoas:
                for pessoa in pessoas:         
                    pessoa_convertida_em_str = json.dumps(pessoa)
                    base_de_dados_das_pessoas.write(f'{pessoa_convertida_em_str}' + '\n')
                return True