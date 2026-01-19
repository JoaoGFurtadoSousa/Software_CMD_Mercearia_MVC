import json
from Categoria.Models import Categoria
from pathlib import Path



BASE_DIR = Path(__file__).parent
ARQUIVO_CATEGORIAS = BASE_DIR / "categorias.txt"


class CategoriaDAO:
    @classmethod
    def ler_todas_as_categorias(cls):
        categorias = []
        ultimo_id = 0
        with open(ARQUIVO_CATEGORIAS, 'r', encoding='utf-8') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                categorias.append(data_em_dict)
                for categoria in categorias:
                     ultimo_id = categoria['id']
            return [categorias, ultimo_id]


    @classmethod
    def salvar_categoria(cls, categoria: Categoria):
            with open(ARQUIVO_CATEGORIAS, 'a') as escrever_no_arquivo:
                try:
                    categoria=categoria.exibir_todos_os_dados_da_instancia()
                    instancia_em_json = json.dumps(categoria)
                    escrever_no_arquivo.writelines(f'{instancia_em_json}\n')
                    return True
                except:
                     return False


    @classmethod
    def buscar_categoria(cls, id: int):
        categorias = []
        categoria_encontrada = None

        with open(ARQUIVO_CATEGORIAS, 'r', encoding='utf-8') as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue

                data = json.loads(linha)
                categorias.append(data)

                if data['id'] == id:
                    categoria_encontrada = data

        if categoria_encontrada:
            return True, categoria_encontrada, categorias

        return False, None, categorias

    @classmethod
    def excluir_categoria(cls, id:int):
        categorias = []
        existe_categoria = True
        with open(ARQUIVO_CATEGORIAS, 'r') as arq:
            for linha in arq: #percorrendo linha a linha do arquivo de produtos 
                linha = linha.strip() # internamente cada linha possui um \n no final. Esse .strip() serve para tirar esse \n e falar que aquela linha chegou ao fim
                data_em_dict = json.loads(linha) #convertendo str para dicionario python
                categorias.append(data_em_dict)
                for categoria in categorias:
                    print(f'Categoria {categoria}')
                    if categoria["id"] == id:
                          categorias.remove(categoria)
                    else:
                        existe_categoria = False                            
        with open(ARQUIVO_CATEGORIAS, 'w') as base_de_dados_de_categorias:
                for categoria in categorias:         
                    categoria_convertido_em_str = json.dumps(categoria)
                    base_de_dados_de_categorias.write(f'{categoria_convertido_em_str}' + '\n')
                return True
  

    
 
    @classmethod
    def atualizar_categoria(cls, id: int, nome: str):
         categorias = []
         existe_categoria, categoria, categorias = cls.buscar_categoria(id= id)
         for categoria in categorias:
                    if categoria["id"] == id:
                          categoria["nome"] = nome
         with open(ARQUIVO_CATEGORIAS, 'w') as base_de_dados_de_categorias:
                for categoria in categorias:         
                    categoria_convertido_em_str = json.dumps(categoria)
                    base_de_dados_de_categorias.write(f'{categoria_convertido_em_str}' + '\n')
                return True