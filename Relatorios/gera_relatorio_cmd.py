from Vendas.Controller import VendasController

controllerVendas = VendasController()


class Relatorios:
    @classmethod
    def relatorio_de_vendas_por_data(cls, data: int):
        vendas = controllerVendas.listar_todos_as_vendas()
        for venda in vendas:
            dia_da_venda = int(venda["data_venda"][8:])
            if dia_da_venda == data:
                print(venda)



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
        print(f"Produto mais vendido: {produto_mais_vendido}")
        print(f"Quantidade de produtos vendidos: {quantidade}")

relatorio = Relatorios()
#relatorio.relatorio_de_vendas_por_data(22)
relatorio.relatorio_produtos_mais_vendidos()
