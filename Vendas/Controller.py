from Vendas.DAO import VendasDAO
from Vendas.Models import Venda
from datetime import datetime
import re



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
    def salvar_venda(cls, id_cliente: int, produtos_vendidos: dict, valor_total:float):
        data = datetime.now()
        data = str(data.date())
        id_venda = VendasDAO.ler_todas_as_vendas()
        id_venda = id_venda[1] + 1 #validar se nenhum campo é nulo
        venda = Venda(id_venda = id_venda, id_cliente=id_cliente ,produtos_vendidos = produtos_vendidos, valor_total= valor_total, data_venda=data)
        return VendasDAO.salvar_venda(venda)
    
    @classmethod
    def listar_todos_as_vendas(cls):
        vendas, _ = VendasDAO.ler_todas_as_vendas()
        return vendas
    
    @classmethod
    def alterar_venda_existente(cls,id_venda: int, id_cliente: int, produtos_vendidos: dict, valor_total:float, data_venda :str):
        cls.listar_todos_as_vendas()
        existe_venda, venda, vendas = VendasDAO.buscar_venda(id= id_venda)
        _ = VendasDAO.atualizar_venda(id_venda= id_venda, 
                                      id_cliente= id_cliente, 
                                      produtos_vendidos=produtos_vendidos, 
                                      valor_total=valor_total,
                                      data_venda = data_venda)
        

    @classmethod
    def excluir_venda(cls, id_venda: int):
        venda_excluida = VendasDAO.excluir_venda(id_venda = id_venda)
        if venda_excluida:
            return True
        return False
    
venda = VendasController()
#venda.salvar_venda(2, {"IDS": [3, 4]}, 1500.0)
"""vendas = venda.listar_todos_as_vendas()
for venda in vendas:
    print(venda)"""
#venda.alterar_venda_existente(2, 3, {"IDS": [5, 6]}, 1700.0, "2026-01-21")
venda.excluir_venda(2)