import controller
import os.path

if __name__ == '__main__':
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Vendedor )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para acessar ( Produtos mais vendidos )\n"
                          "Digite 8 para sair\n"))
        
        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma catedoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para mostrar as categorias\n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar: \n')
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    delCategoria = input('Digite a categoria que deseja remover: \n')
                    cat.removerCategoria(delCategoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar: \n')
                    novaCategoria = input('Digite a nova categoria: \n')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else: 
                    break
        
        if local == 2:
            est = controller.ControllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um produto no estoque: \n'
                                    'Digite 2 para remvoer um produto do estoque: \n'
                                    'Digite 3 para alterar um produto do estoque: \n'
                                    'Digite 4 para mostrar os produtos no estoque: \n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    produto = input('Digite o nome do produto que deseja cadastrar: \n')
                    preco = input('Digite o preco do produto que deseja cadastrar: \n')
                    categoria = input('Digite a categoria do produto que deseja cadastrar: \n')
                    quantidade = input('Digite a quantidade do produto que deseja cadastrar: \n')
                    est.cadastrarProduto(produto, preco, categoria, quantidade)

                elif decidir == 2:
                    delProduto = input('Digite o nome do produto que deseja remvoer: \n')
                    est.removerProduto(delProduto)

                elif decidir == 3:
                    nomeAlterar = input('Digite o nome do produto que deseja alterar: \n')
                    nomeAlterado = input('Digite para qual deseja alterar: \n')
                    preco = input('Digite o preco do produto que deseja cadastrar: \n')
                    categoria = input('Digite a categoria do produto que deseja cadastrar: \n')
                    quantidade = input('Digite a quantidade do produto que deseja cadastrar: \n')
                    est.alterarProduto(nomeAlterar, nomeAlterado, preco, categoria, quantidade)

                elif decidir == 4:
                    est.mostrarProduto()

                else:
                    break
        
        if local == 3:
            fornecedor = controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor: \n"
                                    "Digite 2 para remover um fornecedor: \n"
                                    "Digite 3 para alterar um fornecedor: \n"
                                    "Digite 4 mostrar os fornecedores cadastrados: \n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    nome = input("Digite o nome do fornecedor que deseja cadastrar: \n")
                    cnpj = input("Digite o cnpj do fornecedor: \n")
                    telefone = input("Digite o telefone do fornecedor: \n")
                    categoria = input("Digite a categoria do fornecedor: \n")
                    fornecedor.cadastrarFornecedor(nome, cnpj, telefone, categoria)

                elif decidir == 2:
                    delFornecedor = input("Digite o nome do fornecedor que deseja remover: \n")
                    fornecedor.removerFornecedor(delFornecedor)

                elif decidir == 3:
                    fornecedorAlterar = input("Digite o nome do fornecedor que deseja alterar: \n")
                    fornecedorAlterado = input("Digite o nome do novo fornecedor: \n")
                    cnpj = input("Digite o novo cnpj do fornecedor: \n")
                    telefone = input("Digite o novo telefone do fornecedor: \n")
                    categoria = input("Digite a nova categoria do fornecedor: \n")
                    fornecedor.alterarFornecedor(fornecedorAlterar, fornecedorAlterado, cnpj, telefone, categoria)

                elif decidir == 4:
                    fornecedor.mostrarFornecedores()

                else:
                    break

        if local == 4:
            clientes = controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente: \n"
                                    "Digite 2 para remover um cliente: \n"
                                    "Digite 3 para alterar um cliente: \n"
                                    "Digite 4 para mostrar os clientes cadastrados: \n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    nome = input("Digite o nome do cliente: \n")
                    email = input("Digite o email do cliente: \n")
                    tel = input("Digite o telefone do cliente: \n")
                    cpf = input("Digite o cpf do cliente: \n")
                    endereco = input("Digite o endereço do cliente: \n")
                    clientes.cadastrarCliente(nome, email, tel, cpf, endereco)
                
                elif decidir == 2:
                    delCliente = input("Digite o nome do cliente que deseja remover: \n")
                    clientes.removerCliente(delCliente)

                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do cliente que deseja alterar: \n")
                    nomeAlterado = input("Digite o novo nome do cliente: \n")
                    email = input("Digite o novo email do cliente: \n")
                    tel = input("Digite o novo telefone do cliente: \n")
                    cpf = input("Digite o novo cpf do cliente: \n")
                    endereco = input("Digite o novo endereço do cliente: \n")
                    clientes.alterarCliente(nomeAlterar, nomeAlterado, email, tel, cpf, endereco)

                elif decidir == 4:
                    clientes.mostrarClientes()

                else:
                    break

        if local == 5:
            vendedores = controller.ControllerVendedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um vendedor: \n"
                                    "Digite 2 para remover um vendedor: \n"
                                    "Digite 3 para alterar um vendedor: \n"
                                    "Digite 4 para mostrar os vendedores cadastrados: \n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    nome = input("Digite o nome do vendedor: \n")
                    email = input("Digite o email do vendedor: \n")
                    tel = input("Digite o telefone do vendedor: \n")
                    cpf = input("Digite o cpf do vendedor: \n")
                    endereco = input("Digite o endereço do vendedor: \n")
                    clt = input("Digite o clt do vendedor: \n")
                    vendedores.cadastrarVendedor(nome, email, tel, cpf, endereco, clt)
                
                elif decidir == 2:
                    delVendedor = input("Digite o nome do vendedor que deseja remover: \n")
                    vendedores.removerVendedor(delVendedor)

                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do vendedor que deseja alterar: \n")
                    nomeAlterado = input("Digite o novo nome do vendedor: \n")
                    email = input("Digite o novo email do vendedor: \n")
                    tel = input("Digite o novo telefone do vendedor: \n")
                    cpf = input("Digite o novo cpf do vendedor: \n")
                    endereco = input("Digite o novo endereço do vendedor: \n")
                    clt = input("Digite o novo clt do vendedor: \n")
                    vendedores.alterarVendedor(nomeAlterar, nomeAlterado, email, tel, cpf, endereco, clt)

                elif decidir == 4:
                    vendedores.mostrarVendedores()

                else:
                    break

        if local == 6:
            venda = controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma venda: \n"
                                    "Digite 2 para mostrar as vendas: \n"
                                    "Digite 3 para sair\n"))
                if decidir == 1:
                    produto = input("Digite o produto vendido: \n")
                    vendedor = input("Digite o nome do vendedor: \n")
                    cliente = input("Digite o nome do cliente: \n")
                    qtd = input("Digite a quantidade vendida: \n")
                    venda.cadastrarVenda(produto, vendedor, cliente, qtd)

                elif decidir == 2:
                    dataInicio = input("Digite uma data de inicio: dia/mes/ano\n")
                    dataTermino =input("Digite uma data de termino: dia/mes/ano\n")
                    venda.mostrarVendas(dataInicio, dataTermino)

                else:
                    break

        if local == 7:
            relatorio = controller.ControllerVenda()
            relatorio.relatorioProdutos()
        
        if local == 8:
            break