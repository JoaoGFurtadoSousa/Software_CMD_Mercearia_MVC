from datetime import datetime

class Venda:
    vendas = []

    def __init__(self, id_venda: int, id_cliente: int, produtos_vendidos: dict, valor_total:float, data_venda: str):
        self.id_venda = id_venda
        self.id_cliente = id_cliente
        self.produtos_vendidos = produtos_vendidos
        self.valor_total = valor_total
        self.data_venda = data_venda

    def __str__(self):
        return self.id
    
    def exibir_todos_os_dados_da_instancia(self):
         return self.__dict__
    
