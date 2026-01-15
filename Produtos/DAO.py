import json
from Models import Produto

class ProdutoDAO:
    @classmethod
    def salvar_produto(cls, produto: Produto):
            with open('produtos.txt', 'a') as escrever_no_arquivo:
                try:
                    produto=produto.exibir_todos_os_dados_da_instancia()
                    instancia_em_json = json.dumps(produto)
                    escrever_no_arquivo.writelines(f'{instancia_em_json}\n')
                    return True
                except:
                     print()
                     return False


    @classmethod
    def buscar_produto(cls, id:int):
        produtos = []
        with open('produtos.txt', 'r', encoding='utf-8') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                produtos.append(data_em_dict)
                for produto in produtos:
                     if produto["id"] == id:
                          return True, produto, produtos
        return False, None, None

    @classmethod
    def excluir_produto(cls, id:int):
        produtos = []
        existe_produto = True
        with open('produtos.txt', 'r') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos 
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                produtos.append(data_em_dict)
                for produto in produtos:
                    if produto["id"] == id:
                          produtos.remove(produto)
                          return True
                    existe_produto = False
            return False                       
                        
        with open('produtos.txt', 'w') as base_de_dados_de_produtos:
                for produto in produtos:         
                    produto_convertido_em_str = json.dumps(produto)
                    base_de_dados_de_produtos.write(f'{produto_convertido_em_str}' + '\n')
  

    @classmethod
    def ler_todos_os_produtos(cls):
        produtos = []
        ultimo_id = 0
        with open('produtos.txt', 'r', encoding='utf-8') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                produtos.append(data_em_dict)
                for produto in produtos:
                     ultimo_id = produto['id']
            return [produtos, ultimo_id]
        
    @classmethod
    def 