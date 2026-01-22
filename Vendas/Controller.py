from Vendas.DAO import VendasDAO
from Vendas.Models import Venda
from datetime import datetime
from Produtos.Controller import ProdutosController



controllerProd = ProdutosController()

class VendasController:
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
    def cria_a_data(cls):
        data = datetime.now()
        data = str(data.date())
        return data


    @classmethod
    def salvar_venda(cls, id_cliente: int, produtos_vendidos: dict, valor_total:float):
        data = cls.cria_a_data()
        id_venda = VendasDAO.ler_todas_as_vendas()
        id_venda = id_venda[1] + 1 #validar se nenhum campo é nulo
        venda = Venda(id_venda = id_venda, id_cliente=id_cliente ,produtos_vendidos = produtos_vendidos, valor_total= valor_total, data_venda=data)
        return VendasDAO.salvar_venda(venda)
    
    @classmethod
    def listar_todos_as_vendas(cls):
        vendas, _ = VendasDAO.ler_todas_as_vendas()
        return vendas
    
    @classmethod
    def alterar_venda_existente(cls,id_venda: int, id_cliente: int, produtos_vendidos: dict):
        cls.listar_todos_as_vendas()
        data = cls.cria_a_data()
        valor_total = 0
        existe_venda, venda, vendas = VendasDAO.buscar_venda(id= id_venda)
        if not existe_venda:
            return None
        for produto_unico in produtos_vendidos['id_produtos']:
            produto = controllerProd.buscar_produto_unico(id=produto_unico)
            if not produto:
                return None
            else:
               valor_total += float(produto["preco"])
               retorno_DAO = VendasDAO.atualizar_venda(id_venda= id_venda, 
                                id_cliente= id_cliente, 
                                produtos_vendidos=produtos_vendidos, 
                                valor_total=valor_total,
                                data_venda = data)

        if retorno_DAO is True:
            return True
        return False

        

    @classmethod
    def excluir_venda(cls, id_venda: int):
        venda_excluida = VendasDAO.excluir_venda(id_venda = id_venda)
        if venda_excluida:
            return True
        return False


    @classmethod
    def incrementa_valor_no_caixa(cls, produtos_venda:dict, valor_total_produtos:float):
        while True:
            produto_a_ser_adicionado = int(input("ID do Produto: "))
            produto = controllerProd.buscar_produto_unico(id = produto_a_ser_adicionado)
            valor_total_produtos += float(produto["preco"])
            print(valor_total_produtos)
            produtos_venda["id_produtos"].append(produto_a_ser_adicionado)
            para_de_adicionar_produtos = input("Para sair tecle a letra [S]: ").lower()
            if para_de_adicionar_produtos == "s":
                return produtos_venda, valor_total_produtos
            continue
