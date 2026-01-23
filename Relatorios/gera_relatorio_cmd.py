from Vendas.Controller import VendasController

controllerVendas = VendasController()


class Relatorios:
    @classmethod
    def relatorio_de_vendas_por_data(cls, data: int):
        try:
            vendas = controllerVendas.listar_todos_as_vendas()
            for venda in vendas:
                dia_da_venda = int(venda["data_venda"][8:])
                if dia_da_venda == data:
                    print(venda)
            return True
        except:
            return None

    @classmethod
    def relatorio_produtos_mais_vendidos(cls):
        contador = {}
        vendas = controllerVendas.listar_todos_as_vendas()
        for venda in vendas:
            ids = venda["produtos_vendidos"]["id_produtos"]
            for produto_id in ids:
                if produto_id in contador:
                    contador[produto_id] += 1
                else:
                    contador[produto_id] = 1
        produto_mais_vendido = max(contador, key= contador.get)
        quantidade = contador[produto_mais_vendido]
        print(f"Id do Produto mais vendido: {produto_mais_vendido}")
        print(f"Quantidade de produtos vendidos: {quantidade}")

    @classmethod
    def relatorio_clientes_mais_compraram(cls):
        contador = {}
        vendas = controllerVendas.listar_todos_as_vendas()

        for venda in vendas:
            id_cliente = int(venda["id_cliente"])

            if id_cliente in contador:
                contador[id_cliente] += 1
            else:
                contador[id_cliente] = 1

        cliente_que_mais_comprou = max(contador, key=contador.get)
        quantidade = contador[cliente_que_mais_comprou]
        print(f"ID do Cliente que mais comprou: {cliente_que_mais_comprou}")
        print(f"Quantidade de compras realizadas por esse cliente: {quantidade}")
    
     