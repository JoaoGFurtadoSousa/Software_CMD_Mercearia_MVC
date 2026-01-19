import os, time
from Produtos.Controller import ProdutosController
from Categoria.Controller import CategoriasController
from Fornecedor.Controller import FornecedoresController

controllerProd = ProdutosController()
controllerCateg = CategoriasController()
controllerForn = FornecedoresController()


def limpa_terminal():
    os.system('cls')


def salvar_novo_prod_interface(nome: str, preco: float, fornecedor: str, categoria: str):
    produto = controllerProd.salvar_produto(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
    if produto:
        print("Produto criado com sucesso. 201")
    else:
        print('Erro ao criar o produto. Tente novamente inserindo o formato valido dos dados')

def alterar_prod_interface(nome: str, preco = float, fornecedor = str, categoria = str):
    produto = controllerProd.salvar_produto(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
    if produto:
        print("Produto criado com sucesso. 201")
    else:
        print('Erro ao criar o produto.')

def salvar_nova_categoria_interface(nome: str):
    produto = controllerCateg.salvar_categoria(nome = nome)
    if produto:
        print("Categoria criada com sucesso. 201")
    else:
        print('Erro ao criar a categoria. Tente novamente inserindo o formato valido dos dados')

def alterar_categoria_interface(nome: str):
    categoria = controllerCateg.salvar_categoria(nome = nome)
    if categoria:
        print("Categoria criada com sucesso. 201")
    else:
        print('Erro ao criar a categoria.')

def salvar_novo_fornecedor_interface(nome: str):
    fornecedor = controllerForn.salvar_fornecedor(nome = nome)
    if fornecedor:
        print("Fornecedor criado com sucesso. 201")
    else:
        print('Erro ao criar o Fornecedor. Tente novamente inserindo o formato valido dos dados')

def alterar_fornecedor_interface(nome: str):
    fornecedor = controllerForn.salvar_fornecedor(nome = nome)
    if fornecedor:
        print("Fornecedor criada com sucesso. 201")
    else:
        print('Erro ao criar o Fornecedor.')


def exibir_menu():
    while True:
        escolha_categoria = int(input("Escolha a categoria que deseja:\n [1] Produto \n [2] Categoria \n [3] Fornecedor \n [5] Sair"))
        limpa_terminal()
        match escolha_categoria:
            case 1:
                escolha_usuario = int(input("[1] Listar Produtos \n[2] Salvar Produto \n[3] Alterar Produto \n[4] Excluir Produto \n"))
                limpa_terminal()
                match escolha_usuario:
                    case 1:
                        produtos = controllerProd.listar_todos_os_produtos()
                        for lista_de_produtos in produtos:
                            print(lista_de_produtos)
                    
                    case 2:
                        while True:
                            try:
                                nome = str(input("Nome: ")) 
                                preco= float(input("Valor: "))
                                fornecedor = str(input("Fornecedor: "))
                                categoria = str(input("Categoria: "))
                                validacao_de_campos = controllerProd.verifica_se_ha_campos_nulos(nome = nome, 
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
                        produtos = controllerProd.listar_todos_os_produtos()
                        for lista_de_produtos in produtos:
                            print(lista_de_produtos)
                        while True:
                            produto_que_sera_alterado = int(input("Encaminhe o ID do produto que irá ser alterado: "))
                            nome = str(input("Nome: ")) 
                            preco= float(input("Valor: "))
                            fornecedor = str(input("Fornecedor: "))
                            categoria = str(input("Categoria: "))
                            produto = controllerProd.alterar_produto_existente(id = produto_que_sera_alterado,
                                                                        nome= nome,
                                                                        preco = preco,
                                                                        fornecedor = fornecedor,
                                                                        categoria = categoria)
                            if produto is None:
                                print('Produto com ID não existente. Insira um ID valido')
                                time.sleep(2)
                                limpa_terminal()
                                continue
                            else:
                                print("Produto alterado com sucesso. 200")
                                break
                    case 4:
                        produtos = controllerProd.listar_todos_os_produtos()
                        for lista_de_produtos in produtos:
                            print(lista_de_produtos)
                        while True:
                            produto_que_sera_excluido = int(input("Encaminhe o ID do produto que irá ser alterado: "))
                            produto_que_sera_excluido= controllerProd.excluir_produto(id= produto_que_sera_excluido)
                            if produto_que_sera_excluido:
                                print("Produto excluido com sucesso")
                                break
                            print("Erro ao excluir o produto")
            case 2:
                escolha_usuario = int(input("[1] Listar Categorias \n[2] Salvar Categoria \n[3] Alterar Categoria \n[4] Excluir Categoria \n"))
                limpa_terminal()
                match escolha_usuario:
                    case 1:
                        categoria = controllerCateg.listar_todos_os_categorias()
                        for lista_de_categoria in categoria:
                            print(lista_de_categoria)
                    
                    case 2:
                        while True:
                            try:
                                nome = str(input("Nome: ")) 
                                validacao_de_campos = controllerCateg.verifica_se_ha_campos_nulos(nome = nome)
                                if validacao_de_campos:
                                    salvar_nova_categoria_interface(nome = nome)
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
                        categorias = controllerCateg.listar_todos_os_categorias()
                        for lista_de_categorias in categorias:
                            print(lista_de_categorias)
                        while True:
                            categoria_que_sera_alterada = int(input("Encaminhe o ID do produto que irá ser alterado: "))
                            nome = str(input("Nome: ")) 
                            categoria = controllerCateg.alterar_categoria_existente(id = categoria_que_sera_alterada, nome= nome)
                            if categoria is (False or None):
                                print('Categoria com ID não existente. Insira um ID valido')
                                time.sleep(2)
                                limpa_terminal()
                                continue
                            else:
                                print("Categoria alterada com sucesso. 200")
                                break
                    case 4:
                        categorias = controllerCateg.listar_todos_os_categorias()
                        for lista_de_categorias in categorias:
                            print(lista_de_categorias)
                        while True:
                            categoria_que_sera_excluido = int(input("Encaminhe o ID do produto que irá ser excluido: "))
                            categoria_que_sera_excluido= controllerCateg.excluir_categoria(id= categoria_que_sera_excluido)
                            print(f'Categoria excluida view {categoria_que_sera_excluido}')
                            if categoria_que_sera_excluido:
                                print("Produto excluido com sucesso")
                                break
                            print("Erro ao excluir o produto")
            
            case 3:
                escolha_usuario = int(input("[1] Listar Fornecedores \n[2] Salvar Fornecedor \n[3] Alterar Fornecedor \n[4] Excluir Fornecedor \n"))
                limpa_terminal()
                match escolha_usuario:
                    case 1:
                        fornecedores = controllerForn.listar_todos_os_fornecedores()
                        for lista_de_fornecedores in fornecedores:
                            print(lista_de_fornecedores)
                    
                    case 2:
                        while True:
                            try:
                                nome = str(input("Nome: ")) 
                                validacao_de_campos = controllerForn.verifica_se_ha_campos_nulos(nome = nome)
                                if validacao_de_campos:
                                    salvar_novo_fornecedor_interface(nome = nome)
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
                        fornecedores = controllerForn.listar_todos_os_fornecedores()
                        for lista_de_fornecedores in fornecedores:
                            print(lista_de_fornecedores)
                        while True:
                            fornecedor_que_sera_alterado = int(input("Encaminhe o ID do produto que irá ser alterado: "))
                            nome = str(input("Nome: ")) 
                            fornecedor = controllerForn.alterar_fornecedor_existente(id = fornecedor_que_sera_alterado, nome= nome)
                            if fornecedor is None:
                                print('Fornecedor com ID não existente. Insira um ID valido')
                                time.sleep(2)
                                limpa_terminal()
                                continue
                            else:
                                print("Fornecedor alterado com sucesso. 200")
                                break
                    case 4:
                        fornecedores = controllerForn.listar_todos_os_fornecedores()
                        for lista_de_fornecedores in fornecedores:
                            print(lista_de_fornecedores)
                        while True:
                            fornecedor_que_sera_excluido = int(input("Encaminhe o ID do fornecedor que irá ser alterado: "))
                            fornecedor_que_sera_excluido= controllerForn.excluir_fornecedor(id= fornecedor_que_sera_excluido)
                            print(f' testeeeeee vire{fornecedor_que_sera_excluido}')
                            if fornecedor_que_sera_excluido:
                                print("Fornecedor excluido com sucesso")
                                break
                            print("Erro ao excluir o Fornecedor")
            
            case 5:
                break
    
if __name__ == "__main__":
    exibir_menu()


