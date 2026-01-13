class Produto:
    produtos = []

    def __init__(self, id:int, nome: str, preco:float, fornecedor: str, categoria: str):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.fornecedor = fornecedor
        self.categoria = categoria

    def __str__(self):
            return self.nome
    
    
    def exibir_todos_os_dados_da_instancia(self):
         return self.__dict__
        

