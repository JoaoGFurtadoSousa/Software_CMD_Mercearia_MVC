import json
from Fornecedor.Models import Fornecedor
from pathlib import Path



BASE_DIR = Path(__file__).parent
ARQUIVO_FORNECEDORES = BASE_DIR / "fornecedores.txt"


class FornecedorDAO:
    @classmethod
    def ler_todas_os_fornecedores(cls):
        fornecedores = []
        ultimo_id = 0
        with open(ARQUIVO_FORNECEDORES, 'r', encoding='utf-8') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                fornecedores.append(data_em_dict)
                for fornecedor in fornecedores:
                     ultimo_id = fornecedor['id']
            return [fornecedores, ultimo_id]


    @classmethod
    def salvar_fornecedor(cls, fornecedor: Fornecedor):
            with open(ARQUIVO_FORNECEDORES, 'a') as escrever_no_arquivo:
                try:
                    fornecedor=fornecedor.exibir_todos_os_dados_da_instancia()
                    instancia_em_json = json.dumps(fornecedor)
                    escrever_no_arquivo.writelines(f'{instancia_em_json}\n')
                    return True
                except:
                     return False


    @classmethod
    def buscar_fornecedor(cls, id: int):
        fornecedores = []
        fornecedor_encontrado = None

        with open(ARQUIVO_FORNECEDORES, 'r', encoding='utf-8') as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue

                data = json.loads(linha)
                fornecedores.append(data)

                if data['id'] == id:
                    fornecedor_encontrado = data

        if fornecedor_encontrado:
            return True, fornecedor_encontrado, fornecedores

        return False, None, fornecedores

    @classmethod
    def excluir_fornecedor(cls, id:int):
        fornecedores = []
        existe_fornecedor = True
        with open(ARQUIVO_FORNECEDORES, 'r') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos 
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                fornecedores.append(data_em_dict)
                for fornecedor in fornecedores:
                    print(f'Fornecedor {fornecedor}')
                    if fornecedor["id"] == id:
                          fornecedores.remove(fornecedor)
                    else:
                        existe_fornecedor = False                            
        with open(ARQUIVO_FORNECEDORES, 'w') as base_de_dados_de_fornecedores:
                for fornecedor in fornecedores:         
                    fornecedor_convertido_em_str = json.dumps(fornecedor)
                    base_de_dados_de_fornecedores.write(f'{fornecedor_convertido_em_str}' + '\n')
                return True
  

    
 
    @classmethod
    def atualizar_fornecedor(cls, id: int, nome: str):
         fornecedores = []
         existe_fornecedor, fornecedor, fornecedores = cls.buscar_fornecedor(id= id)
         for fornecedor in fornecedores:
                    if fornecedor["id"] == id:
                          fornecedor["nome"] = nome
         with open(ARQUIVO_FORNECEDORES, 'w') as base_de_dados_de_fornecedores:
                for fornecedor in fornecedores:         
                    fornecedor_convertido_em_str = json.dumps(fornecedor)
                    base_de_dados_de_fornecedores.write(f'{fornecedor_convertido_em_str}' + '\n')
                return True