import os, time
from Categoria.Controller import CategoriasController

controller = CategoriasController()

def limpa_terminal():
    os.system('cls')


def salvar_novo_prod_interface(nome: str):
    categoria = controller.salvar_categoria(nome = nome)
    if categoria:
        print("Categoria criada com sucesso. 201")
    else:
        print('Erro ao criar a categoria. Tente novamente inserindo o formato valido dos dados')

def alterar_categ_interface(nome: str):
    categoria = controller.salvar_categoria(nome = nome)
    if categoria:
        print("Categoria criada com sucesso. 201")
    else:
        print('Erro ao criar o categoria.')



def exibir_menu():
    categoriaDef = int(input("Escolha a categoria que deseja:\n [1] Produto "))
    limpa_terminal()
    match categoriaDef:
        case 1:
            escolha_usuario = int(input("[1] Listar Produtos \n[2] Salvar Produto \n[3] Alterar Produto \n[4] Excluir Produto \n"))
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
                            validacao_de_campos = controller.verifica_se_ha_campos_nulos(nome = nome, 
                                                                                         preco = preco, 
                                                                                         fornecedor = fornecedor, 
                                                                                         categoria = categoria)
                            if validacao_de_campos:
                                salvar_novo_prod_interface(nome = nome, 
                                                           preco = preco, 
                                                           fornecedor = fornecedor, 
                                                           categoria = categoria)
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
                        nome = str(input("Nome: ")) 
                        preco= float(input("Valor: "))
                        fornecedor = str(input("Fornecedor: "))
                        categoria = str(input("Categoria: "))
                        produto = controller.alterar_produto_existente(id = produto_que_sera_alterado,
                                                                       nome= nome,
                                                                       preco = preco,
                                                                       fornecedor = fornecedor,
                                                                       categoria = categoria)
                        if produto is False:
                            print('Produto com ID não existente. Insira um ID valido')
                            break
                        else:
                            print("Produto alterado com sucesso. 200")
                            break
                case 4:
                    produtos = controller.listar_todos_os_produtos()
                    for lista_de_produtos in produtos:
                        print(lista_de_produtos)
                    while True:
                        produto_que_sera_excluido = int(input("Encaminhe o ID do produto que irá ser alterado: "))
                        produto_que_sera_excluido= controller.excluir_produto(id= produto_que_sera_excluido)
                        if produto_que_sera_excluido:
                            print("Produto excluido com sucesso")
                            break
                        print("Erro ao excluir o produto")
                

if __name__ == "__main__":
    exibir_menu()


