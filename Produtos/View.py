import os, time, json
from Produtos.Controller import ProdutosController
from Categoria.Controller import CategoriasController
from Fornecedor.Controller import FornecedoresController
from Clientes.Controller import ClientesController
from Funcionarios.Controller import FuncionariosController
from Vendas.Controller import VendasController
from Relatorios.gera_relatorio_cmd import Relatorios


controllerProd = ProdutosController()
controllerCateg = CategoriasController()
controllerForn = FornecedoresController()
controllerClientes = ClientesController()
controllerFunc = FuncionariosController()
controllerVendas = VendasController()
relatorio = Relatorios()


def limpa_terminal():
    os.system('cls')


def salvar_novo_prod_interface(nome: str, preco: float, fornecedor: str, categoria: str):
    produto = controllerProd.salvar_produto(nome = nome, preco = preco, fornecedor = fornecedor, categoria = categoria)
    if produto:
        print("Produto criado com sucesso. 201")
    else:
        print('Erro ao criar o produto. Tente novamente inserindo o formato valido dos dados')


def salvar_nova_categoria_interface(nome: str):
    produto = controllerCateg.salvar_categoria(nome = nome)
    if produto:
        print("Categoria criada com sucesso. 201")
    else:
        print('Erro ao criar a categoria. Tente novamente inserindo o formato valido dos dados')


def salvar_novo_fornecedor_interface(nome: str):
    fornecedor = controllerForn.salvar_fornecedor(nome = nome)
    if fornecedor:
        print("Fornecedor criado com sucesso. 201")
    else:
        print('Erro ao criar o Fornecedor. Tente novamente inserindo o formato valido dos dados')


def salvar_novo_cliente_interface(nome: str, cpf:str, email:str):
    cliente = controllerClientes.salvar_cliente(nome = nome, cpf= cpf, email= email)
    if cliente:
        print("Cliente criado com sucesso. 201")
    else:
        print('Erro ao criar o Cliente. Tente novamente inserindo o formato valido dos dados')

def salvar_novo_funcionario_interface(nome: str, cpf:str, email:str):
    funcionario = controllerFunc.salvar_funcionario(nome = nome, cpf= cpf, email= email)
    if funcionario:
        print("Funcionario criado com sucesso. 201")
    else:
        print('Erro ao criar o Funcionario. Tente novamente inserindo o formato valido dos dados')

def salvar_nova_venda_interface(id_cliente: int, produtos_vendidos: dict, valor_total:float):
    venda = controllerVendas.salvar_venda(id_cliente=id_cliente, produtos_vendidos= produtos_vendidos, valor_total= valor_total)
    if venda:
        print("Venda criada com sucesso. 201")
    else:
        print('Erro ao criar a Venda. Tente novamente inserindo o formato valido dos dados')


def exibir_menu():
    while True:
        escolha_categoria = int(input("Escolha a categoria que deseja:" \
        "\n [1] Produto " \
        "\n [2] Categoria " \
        "\n [3] Fornecedor " \
        "\n [4] Clientes " \
        "\n [5] Funcionarios " \
        "\n [6] Caixa " \
        "\n [7] Relatorios " \
        "\n [8] Sair"))
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
                                print("Categoria excluido com sucesso")
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
                            fornecedor_que_sera_excluido = int(input("Encaminhe o ID do fornecedor que irá ser excluido: "))
                            fornecedor_que_sera_excluido= controllerForn.excluir_fornecedor(id= fornecedor_que_sera_excluido)
                            if fornecedor_que_sera_excluido:
                                break
                            print("Erro ao excluir o Fornecedor")
            case 4:
                escolha_usuario = int(input("[1] Listar Clientes \n[2] Salvar Clientes \n[3] Alterar Clientes \n[4] Excluir Clientes \n"))
                limpa_terminal()
                match escolha_usuario:
                    case 1:
                        pessoas = controllerClientes.listar_todos_as_pessoas()
                        for lista_de_pessoas in pessoas:
                            print(lista_de_pessoas)
                    
                    case 2:
                        while True:
                            try:
                                nome = str(input("Nome: "))
                                cpf = str(input("CPF: "))
                                email = str(input("Email: "))
                                validacao_de_campos = controllerClientes.verifica_veracidade_dos_dados_inseridos(nome = nome,
                                                                                                                 cpf= cpf,
                                                                                                                 email= email)
                                if validacao_de_campos:
                                    salvar_novo_cliente_interface(nome = nome, cpf= cpf, email= email)
                                    break
                                print("Valores estão invalidos")
                                time.sleep(2)
                                limpa_terminal() 
                                continue
                            except ValueError as err:
                                print(f"Valor da variavel {err} está no formato incorreto.")
                                time.sleep(2)
                                limpa_terminal()
                                
                    
                    case 3:
                        clientes = controllerClientes.listar_todos_as_pessoas()
                        for lista_de_pessoas in clientes:
                            print(lista_de_pessoas)
                        while True:
                            cliente_que_sera_alterado = int(input("Encaminhe o ID do cliente que irá ser alterado: "))
                            nome = str(input("Nome: "))
                            cpf = str(input("CPF: "))
                            email = str(input("Email: "))
                            cliente, existe_pessoa = controllerClientes.alterar_pessoa_existente(id = cliente_que_sera_alterado, 
                                                                                  nome= nome,
                                                                                  cpf= cpf,
                                                                                  email= email)
                            print(f"Existe pessoa dentro da view return {existe_pessoa}")
                            if cliente is False and existe_pessoa is False:
                                print('Cliente com ID não existente. Insira um ID valido')
                                time.sleep(6)
                                limpa_terminal()
                                continue
                            elif cliente is False and existe_pessoa is True:
                                time.sleep(6)
                                limpa_terminal()
                                continue
                            else:
                                print("Cliente alterado com sucesso. 200")
                                break
                    case 4:
                        clientes = controllerClientes.listar_todos_as_pessoas()
                        for lista_de_pessoas in clientes:
                            print(lista_de_pessoas)
                        while True:
                            cliente_que_sera_excluido = int(input("Encaminhe o ID do cliente que irá ser excluido: "))
                            cliente_que_sera_excluido= controllerClientes.excluir_pessoa(id= cliente_que_sera_excluido)
                            if cliente_que_sera_excluido:
                                print("Cliente excluido com sucesso")
                                break
                            print("Erro ao excluir o Cliente")
            
            case 5:
                escolha_usuario = int(input("[1] Listar Funcionarios \n[2] Salvar Funcionario \n[3] Alterar Funcionario \n[4] Excluir Funcionario \n"))
                limpa_terminal()
                match escolha_usuario:
                    case 1:
                        pessoas = controllerFunc.listar_todos_as_pessoas()
                        for lista_de_pessoas in pessoas:
                            print(lista_de_pessoas)
                    
                    case 2:
                        while True:
                            try:
                                nome = str(input("Nome: "))
                                cpf = str(input("CPF: "))
                                email = str(input("Email: "))
                                validacao_de_campos = controllerFunc.verifica_veracidade_dos_dados_inseridos(nome = nome,
                                                                                                             cpf= cpf,
                                                                                                             email= email)
                                if validacao_de_campos:
                                    salvar_novo_funcionario_interface(nome = nome, cpf= cpf, email= email)
                                    break
                                print("Valores estão invalidos")
                                time.sleep(2)
                                limpa_terminal() 
                                continue
                            except ValueError as err:
                                print(f"Valor da variavel {err} está no formato incorreto.")
                                time.sleep(2)
                                limpa_terminal()
                                
                    
                    case 3:
                        funcionarios = controllerFunc.listar_todos_as_pessoas()
                        for lista_de_pessoas in funcionarios:
                            print(lista_de_pessoas)
                        while True:
                            funcionario_que_sera_alterado = int(input("Encaminhe o ID do funcionario que irá ser alterado: "))
                            nome = str(input("Nome: "))
                            cpf = str(input("CPF: "))
                            email = str(input("Email: "))
                            funcionario, existe_pessoa = controllerFunc.alterar_pessoa_existente(id = funcionario_que_sera_alterado, 
                                                                                  nome= nome,
                                                                                  cpf= cpf,
                                                                                  email= email)
                            if funcionario is False and existe_pessoa is False:
                                print('Funcionario com ID não existente. Insira um ID valido')
                                time.sleep(6)
                                limpa_terminal()
                                continue
                            elif funcionario is False and existe_pessoa is True:
                                time.sleep(6)
                                limpa_terminal()
                                continue
                            else:
                                print("Funcionario alterado com sucesso. 200")
                                break
                    case 4:
                        funcionarios = controllerFunc.listar_todos_as_pessoas()
                        for lista_de_pessoas in funcionarios:
                            print(lista_de_pessoas)
                        while True:
                            funcionario_que_sera_excluido = int(input("Encaminhe o ID do funcionario que irá ser excluido: "))
                            funcionario_que_sera_excluido= controllerFunc.excluir_pessoa(id= funcionario_que_sera_excluido)
                            if funcionario_que_sera_excluido:
                                print("Funcionario excluido com sucesso")
                                break
                            print("Erro ao excluir o Funcionario")

            case 6:
                escolha_usuario = int(input("[1] Listar Vendas \n[2] Nova Venda \n[3] Alterar Venda \n[4] Excluir Venda \n"))
                limpa_terminal()
                match escolha_usuario:
                    case 1:
                        vendas = controllerVendas.listar_todos_as_vendas()
                        for lista_de_vendas in vendas:
                            print(lista_de_vendas)
                    
                    case 2:
                        produtos_venda = {"id_produtos": []}
                        valor_total_produtos = 0
                        while True:
                            try:
                                lista_de_produtos = controllerProd.listar_todos_os_produtos()
                                id_cliente = int(input("ID Cliente: "))
                                limpa_terminal() 
                                for produto in lista_de_produtos:
                                    print(produto)
                                produtos_venda, valor_total_produtos = controllerVendas.incrementa_valor_no_caixa(produtos_venda= produtos_venda,
                                                                                                                  valor_total_produtos=valor_total_produtos)
                                validacao_de_campos = controllerVendas.verifica_se_ha_campos_nulos(id_cliente = id_cliente, 
                                                                                                   produtos_venda = produtos_venda,
                                                                                                   valor_total_produtos= valor_total_produtos)
                                if validacao_de_campos:
                                    salvar_nova_venda_interface(id_cliente = id_cliente, produtos_vendidos= produtos_venda, valor_total = valor_total_produtos )
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
                        produtos_venda = {"id_produtos": []}
                        vendas = controllerVendas.listar_todos_as_vendas()
                        for lista_de_vendas in vendas:
                            print(lista_de_vendas)
                        while True:
                            venda_que_sera_alterada = int(input("Encaminhe o ID da venda que será alterada: "))
                            id_cliente = int(input("ID Cliente: ")) 
                            entrada = input("Produtos vendidos (ex: 7,5): ")
                            ids_produtos = [int(id.strip()) for id in entrada.split(',')]
                            produtos_venda = {
                            "id_produtos": ids_produtos
                            }
                            venda = controllerVendas.alterar_venda_existente(id_venda = venda_que_sera_alterada,
                                                                        id_cliente = id_cliente,
                                                                        produtos_vendidos = produtos_venda,
                                                                        )
                            if venda is None:
                                print('Venda com ID não existente. Insira um ID valido')
                                time.sleep(5)
                                limpa_terminal()
                                continue
                            else:
                                print("Venda alterada com sucesso. 200")
                                break
                    case 4:
                        vendas = controllerVendas.listar_todos_as_vendas()
                        for lista_de_vendas in vendas:
                            print(lista_de_vendas)
                        while True:
                            venda_que_sera_excluida = int(input("Encaminhe o ID da venda que irá ser excluida: "))
                            venda_que_sera_excluida= controllerVendas.excluir_venda(id_venda= venda_que_sera_excluida)
                            if venda_que_sera_excluida:
                                print("Venda excluida com sucesso")
                                break
                            print("Erro ao excluir a venda")
            
            case 7:
                escolha_usuario = int(input("Escolha o relatorio desejado:\n [1]Relatorio por data \n [2]Relatorio de produtos mais vendidos \n"\
            " [3]Relatorio de clientes que mais compraram"))
                match escolha_usuario:
                    case 1:
                       while True:
                        data = int(input("Data da consulta: "))
                        resultado_relatorio = relatorio.relatorio_de_vendas_por_data(data= data)
                        print(resultado_relatorio)
                        if resultado_relatorio is None:
                            print("Não existe vendas nessa data.")
                            continue
                        break
                       
                    case 2:
                        relatorio.relatorio_produtos_mais_vendidos()

                    case 3:
                        relatorio.relatorio_clientes_mais_compraram()
                

            case 8:
                break
    
if __name__ == "__main__":
    exibir_menu()


