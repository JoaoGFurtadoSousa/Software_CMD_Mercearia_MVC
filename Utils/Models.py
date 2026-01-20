class Pessoa:
    fornecedores = []

    def __init__(self, id:int, nome: str, cpf:str, email:str, tipo_pessoa: dict):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tipo_pessoa = tipo_pessoa

    def __str__(self):
            return self.email
    
    
    def exibir_todos_os_dados_da_instancia(self):
         return self.__dict__
        

