import json
from Vendas.Models import Venda
from pathlib import Path


BASE_DIR = Path(__file__).parent
ARQUIVO_VENDAS = BASE_DIR / f"vendas.txt"


class VendasDAO:
    @classmethod
    def ler_todas_as_vendas(cls):
        vendas = []
        ultimo_id = 0
        with open(ARQUIVO_VENDAS, 'r', encoding='utf-8') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                vendas.append(data_em_dict)
                for venda in vendas:
                     ultimo_id = venda['id_venda']
            return [vendas, ultimo_id]


    @classmethod
    def salvar_venda(cls, venda: Venda):
            with open(ARQUIVO_VENDAS, 'a') as escrever_no_arquivo:
                try:
                    venda = venda.exibir_todos_os_dados_da_instancia()
                    instancia_em_json = json.dumps(venda)
                    escrever_no_arquivo.writelines(f'{instancia_em_json}\n')
                    return True
                except:
                     return False


    @classmethod
    def buscar_venda(cls, id: int):
        vendas = []
        venda_encontrada = None

        with open(ARQUIVO_VENDAS, 'r', encoding='utf-8') as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue

                data = json.loads(linha)
                vendas.append(data)

                if data['id_venda'] == id:
                    venda_encontrada = data

        if venda_encontrada:
            return True, venda_encontrada, vendas

        return False, None, vendas

    @classmethod
    def excluir_venda(cls, id_venda:int):
        vendas = []
        existe_venda = True
        with open(ARQUIVO_VENDAS, 'r') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos 
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                vendas.append(data_em_dict)
                for venda in vendas:
                    if venda["id_venda"] == id_venda:
                          vendas.remove(venda)
                    else:
                        existe_venda = False                            
        with open(ARQUIVO_VENDAS, 'w') as base_de_dados_das_vendas:
                for venda in vendas:         
                    venda_convertida_em_str = json.dumps(venda)
                    base_de_dados_das_vendas.write(f'{venda_convertida_em_str}' + '\n')
                return True
  

    
 
    @classmethod
    def atualizar_venda(cls, id_venda: int, id_cliente: int, produtos_vendidos: dict, valor_total: float, data_venda: str):
         vendas = []
         existe_venda, venda, vendas = cls.buscar_venda(id= id_venda)
         if existe_venda:
            for venda in vendas:
                        if venda["id_venda"] == id_venda:
                            venda["id_cliente"] = id_cliente
                            venda["produtos_vendidos"] = produtos_vendidos
                            venda["valor_total"] = valor_total
                            venda["data_venda"] = data_venda
            with open(ARQUIVO_VENDAS, 'w') as base_de_dados_das_vendas:
                    for venda in vendas:         
                        venda_convertida_em_str = json.dumps(venda)
                        base_de_dados_das_vendas.write(f'{venda_convertida_em_str}' + '\n')
            return True
         return False