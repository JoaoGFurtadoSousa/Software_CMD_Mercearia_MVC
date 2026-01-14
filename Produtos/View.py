import os
from Controller import ProdutosController

controller = ProdutosController()

def limpa_terminal():
    os.system('cls')


def salvar_novo_prod_interface(nome: str, preco: float, fornecedor: str, categoria: str):
    produto = controller.salvar_produto(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
    if produto:
        print("Produto criado com sucesso. 201")
    else:
        print('Erro ao criar o produto.')

def alterar_prod_interface(nome: str, preco: float, fornecedor: str, categoria: str):
    produto = controller.salvar_produto(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
    if produto:
        print("Produto criado com sucesso. 201")
    else:
        print('Erro ao criar o produto.')



def exibir_menu():
    categoria = int(input("Escolha a categoria que deseja:\n [1] Produto "))
    limpa_terminal()
    match categoria:
        case 1:
            escolha_usuario = int(input("[1] Listar Produtos \n[2] Salvar Produto \n[3] Alterar Produto"))
            match escolha_usuario:
                case 1:
                    produtos = controller.listar_todos_os_produtos()
                    for lista_de_produtos in produtos:
                        print(lista_de_produtos)
                
                case 2:
                    nome = str(input("Nome: ")) 
                    preco= float(input("Valor: "))
                    fornecedor = str(input("Fornecedor: "))
                    categoria = str(input("Categoria: "))
                    salvar_novo_prod_interface(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
                
                case 3:
                    controller.alterar_produto_existente(2)
                    
                

if __name__ == "__main__":
    exibir_menu()


