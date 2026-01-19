class Fornecedor:
    fornecedores = []

    def __init__(self, id:int, nome: str):
        self.id = id
        self.nome = nome

    def __str__(self):
            return self.nome
    
    
    def exibir_todos_os_dados_da_instancia(self):
         return self.__dict__
        

