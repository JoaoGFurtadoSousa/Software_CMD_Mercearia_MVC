import json
from Models import Produto

class ProdutoDAO:
    @classmethod
    def salvar_produto(cls, id:int, nome: str, preco:float, fornecedor: str, categoria: str):
            with open('produtos.txt', 'a') as escrever_no_arquivo:
                novo_objeto = Produto(id, nome, preco, fornecedor, categoria)
                todas_as_informacoes_da_instancia = novo_objeto.exibir_todos_os_dados_da_instancia()
                Produto.produtos.append(todas_as_informacoes_da_instancia)
                instancia_em_json = json.dumps(todas_as_informacoes_da_instancia)
                escrever_no_arquivo.writelines(f'{instancia_em_json}\n')

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
                          print(produto)

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
                          print('Produto removido com sucesso')
                    existe_produto = False
            print('Produto com esse ID não existe')                       
                        
        with open('produtos.txt', 'w') as base_de_dados_de_produtos:
                for produto in produtos:         
                    produto_convertido_em_str = json.dumps(produto)
                    base_de_dados_de_produtos.write(f'{produto_convertido_em_str}' + '\n')

1
  

#produto = ProdutoDAO.salvar_produto(2, "dsadasdP", 600.0, "Sony", "Videogames")
pesquisa = ProdutoDAO.excluir_produto(3)

        