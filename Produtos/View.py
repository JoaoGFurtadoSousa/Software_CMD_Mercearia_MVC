import os, time
from Controller import ProdutosController

controller = ProdutosController()

def limpa_terminal():
    os.system('cls')


def salvar_novo_prod_interface(nome: str, preco: float, fornecedor: str, categoria: str):
    produto = controller.salvar_produto(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
    if produto:
        print("Produto criado com sucesso. 201")
    else:
        print('Erro ao criar o produto. Tente novamente inserindo o formato valido dos dados')

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
            limpa_terminal()
            match escolha_usuario:
                case 1:
                    produtos = controller.listar_todos_os_produtos()
                    for lista_de_produtos in produtos:
                        print(lista_de_produtos)
                
                case 2:
                    while True:
                        try:
                            nome = str(input("Nome: ")) 
                            preco= float(input("Valor: "))
                            fornecedor = str(input("Fornecedor: "))
                            categoria = str(input("Categoria: "))
                            validacao_de_campos = controller.verifica_se_ha_campos_nulos(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
                            print(validacao_de_campos)
                            if validacao_de_campos:
                                salvar_novo_prod_interface(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
                                break
                            print("Valores nulos não são permitidos")
                            time.sleep(2)
                            limpa_terminal() 
                            continue
                        except ValueError as err:
                            print(f"Valor da variavel {err} está no formato incorreto.")
                            time.sleep(2)
                            limpa_terminal()
                            
                
                case 3:
                    produtos = controller.listar_todos_os_produtos()
                    for lista_de_produtos in produtos:
                        print(lista_de_produtos)
                    while True:
                        produto_que_sera_alterado = int(input("Encaminhe o ID do produto que irá ser alterado: "))
                        produto = controller.alterar_produto_existente(produto_que_sera_alterado)
                        if produto is False:
                            print('Produto com ID não existente. Insira um ID valido')
                        break
                

if __name__ == "__main__":
    exibir_menu()


