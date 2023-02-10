from models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Vendedor, Venda
from dao import CategoriaDao, EstoqueDao, VendedorDao, PessoaDao, VendaDao, FornecedorDao
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = CategoriaDao.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            CategoriaDao.salvar(novaCategoria)
            print('Categoria Cadastrada com sucesso!')
        else:
            print('Categoria já existe')
    
    def removerCategoria(self, delCategoria):
        x = CategoriaDao.ler()
        cat = list(filter(lambda x: x.categoria == delCategoria, x))
        
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe!')
        else: 
            for i in range(len(x)):
                if x[i].categoria == delCategoria:
                    del x[i]
                    break
            print('Categoria removida!')
            with open('./arq/categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = EstoqueDao.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome_p, x.produto.preco, "Sem categoria"), x.quantidade) if(x.produto.categoria == delCategoria) else(x), estoque))
        with open('./arq/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome_p + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = CategoriaDao.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('Alteração feita com sucesso!')
            #TODO: ALTERAR A CATEGORIA NO ESTOQUE
            else:
                print('A categoria que deseja alterar já existe!')

        else:
            print('A categoria q deseja alterar não existe!')

        with open('./arq/categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
        estoque = EstoqueDao.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome_p, x.produto.preco, categoriaAlterada), x.quantidade) if(x.produto.categoria == categoriaAlterar) else(x), estoque))
        with open('./arq/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome_p + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')


    def mostrarCategoria(self):
        categorias = CategoriaDao.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        if len(categorias) > 0:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome_p == nome, x)) #ta dando erro aq nao sei oq fazer
        
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                EstoqueDao.salvar(produto, quantidade)
                print('Produto Cadastrado com sucesso!')
            else:
                print('Este produto já existe')
        else:
            print('Categoria inexistente')
    
    def removerProduto(self, delProduto):
        x = EstoqueDao.ler()
        stock = list(filter(lambda x: x.produto.nome_p == delProduto, x))
        if len(stock) <= 0:
            print('O produto q deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i].produto.nome_p == delProduto:
                    del x[i]
                    print('Produto removido do estoque!')
                    break
        with open('./arq/estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome_p + '|' + i.produto.preco + '|' + 
                           i.produto.categoria + '|' + str(i.quantidade))
            
                arq.writelines('\n')

    def alterarProduto(self, produtoAlterar, produtoAlterado, novoPreco, novaCategoria, novaQuantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            stock = list(filter(lambda x: x.produto.nome_p == produtoAlterar, x))
            if len(stock) > 0:
                stock1 = list(filter(lambda x: x.produto.nome_p == produtoAlterado, x))
                if len(stock1) == 0:
                    x = list(map(lambda x: Estoque(Produtos(produtoAlterado, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome_p == produtoAlterar) else(x), x))
                    print("Produto alterado com sucesso!")
                else:
                    print('O produto q deseja alterar já existe!')
            else:
                print('O produto que deseja alterar não existe!')
            
            with open('./arq/estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome_p + '|' + i.produto.preco + '|' + 
                           i.produto.categoria + '|' + str(i.quantidade))
                
                    arq.writelines('\n')
        else:
            print('A categoria do produto q deseja alterar não existe!')

    def mostrarProduto(self):
        estoque = EstoqueDao.ler()
        if len(estoque) <= 0:
            print('Estoque vazio!')
        else:
            for i in estoque:
                print(f' Produto: {i.produto.nome_p} | Preço: {i.produto.preco}R$ | Categoria: {i.produto.categoria} | Quantidade: {i.quantidade}')            
            

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        estoque = EstoqueDao.ler()
        temp = []
        existe = False
        quantidade = False
        for i in estoque:
            if existe == False:
                if i.produto.nome_p == nomeProduto:
                    existe = True
                    if i.quantidade >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produtos(i.produto.nome_p, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorVenda = int(i.produto.preco) * int(quantidadeVendida)

                        VendaDao.salvar(vendido)
            temp.append([Produtos(i.produto.nome_p, i.produto.preco, i.produto.categoria), i.quantidade])
        arq = open('./arq/estoque.txt', 'w')
        arq.writelines("")

        for i in temp:
            with open('./arq/estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome_p + "|" + i[0].preco + "|" + i[0].categoria + "|" + str(i[1]))
                arq.writelines('\n')

        if existe == False:
            print('Produto não existe!')
            return None
        elif not quantidade:
            print('A quantidade vendida não tem em estoque')
        else:
            print('Venda realizada com sucesso!')
            return valorVenda

    def relatorioProdutos(self):
        vendas = VendaDao.ler()
        produtos = []
        for i in vendas:
            nome = i.itemVendido.nome_p
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] ==  nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                                    if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
        
        ordenado = sorted(produtos, key = lambda k: k['quantidade'], reverse=True)
        print('Estes são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f"========== Produto {a} ==========")
            print(f"Produto: {i['produto']} \n"
                  f"Quantidade: {i['quantidade']} \n")
            a += 1

    def mostrarVendas(self, dataInicio1, dataTermino1): #vendas em uma determinada data, entre uma e outra. 
        vendas = VendaDao.ler()
        dataInicio1 = datetime.strptime(dataInicio1, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino1, '%d/%m/%Y')
        if len(vendas) <= 0:
            print('nenhuma venda!')
        else:
            vendaData = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))
            cont = 1
            total= 0
            for i in vendaData:
                print(f'==========Venda {cont}==========')
                print(f'Produto: {i.itemVendido.nome_p}\n'
                      f'Categoria: {i.itemVendido.categoria}\n'
                      f'Data: {i.data}\n'
                      f'Quantidade: {i.quantidadeVendida}\n'
                      f'Cliente: {i.cliente}\n'
                      f'Vendedor: {i.vendedor}')
                total = int(i.itemVendido.preco) * int(i.quantidadeVendida)
                cont += 1
            print(f'Total: {total}')

class ControllerFornecedor:
    def cadastrarFornecedor(self, nome_f, cnpj, telefone, categoria):
        x = FornecedorDao.ler()
        listarCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listarTel = list(filter(lambda x: x.telefone == telefone, x))
        if len(listarCnpj) > 0:
            print("Esse cnpj já esta cadastrado!")
        elif len(listarTel) > 0:
            print("Esse telefone já esta cadastrado!")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                FornecedorDao.salvar(Fornecedor(nome_f, cnpj, telefone, categoria))
                print("Fornecedor cadastrado com sucesso!")
            else:
                print("Digite um cnpj ou telefone válidos")

    def removerFornecedor(self, delFornecedor):
        x = FornecedorDao.ler()
        fornecedores = list(filter(lambda x: x.nome_f == delFornecedor, x))
        if len(fornecedores) <= 0:
            print("Fornecedor que deseja remover não está cadastrado!")
            return None #tenta apagar caso de ruim
        else:
            for i in range(len(x)):
                if x[i].nome_f == delFornecedor:
                    del x[i]
                    print("Fornecedor removido do sistema")
                    break
        with open('./arq/fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome_f + '|' + i.cnpj + '|' + 
                            i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')

    def alterarFornecedor(self, nomeAlterar, nomeAlterado, novoCnpj, novoTel, novaCategoria):
        x = FornecedorDao.ler()
        fornecedores = list(filter(lambda x: x.nome_f == nomeAlterar, x))
        if len(fornecedores) > 0:
            fornecedores1 = list(filter(lambda x: x.nome_f == nomeAlterado, x))
            if len(fornecedores1) == 0:
                x = list(map(lambda x: Fornecedor(nomeAlterado, novoCnpj, novoTel, novaCategoria) if(x.nome_f == nomeAlterar) else(x), x))
                print("Fornecedor alterado com sucesso!")
            else:
                print("O fornecedor que deseja alterar já existe!")
            with open ('./arq/fornecedor.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.nome_f + '|' + i.cnpj + '|' + 
                            i.telefone + '|' + i.categoria)
                    arq.writelines('\n')
        else:
         print("O Fornecedor que deseja alterar não existe!")

    def mostrarFornecedores(self):
        x = FornecedorDao.ler()
        if len(x) <= 0:
            print("Nenhum fornecedor cadastrado!")
        else:
            for i in x:
                print("==========Fornecedores==========")
                print(f'Fornecedor: {i.nome_f}\n'
                      f'Cnpj: {i.cnpj}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Categoria: {i.categoria}')

class ControllerCliente:
    def cadastrarCliente(self, nome, email, tel, cpf, endereco):
        x = PessoaDao.ler()
        lerCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(lerCpf) > 0:
            print('Cpf já cadastrado!')
        else:
            if len(cpf) == 11 and len(tel) <= 11 and len(tel) >= 10:
                PessoaDao.salvar(Pessoa(nome, email, tel, cpf, endereco))
                print("Cliente cadastrado com sucesso!")
            else:
                print("Digite um cpf ou telefone válido")

    def removerCliente(self, delCliente):
        x = PessoaDao.ler()
        pessoas = list(filter(lambda x: x.nome == delCliente, x))
        if len(pessoas) == 0:
            print("O Cliente q deseja remover não está cadastrado no sistema!")
            return None #tenta apagar caso de ruim
        else:
            for i in range(len(x)):
                if x[i].nome == delCliente:
                    del x[i]
                    print("Cliente removido com sucesso!")
                    break
        
        with open('./arq/pessoas.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.email + '|' + i.telefone + '|' +
                            i.cpf + '|' + i.endereco)
                arq.writelines('\n')

    def alterarCliente(self, nomeAlterar, nomeAlterado, novoEmail, novoTel, novoCpf, novoEndereco):
        x = PessoaDao.ler()
        pessoas = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(pessoas) > 0:
            pessoas1 = list(filter(lambda x: x.nome == nomeAlterado, x))
            if len(pessoas1) == 0:
                x = list(map(lambda x: Pessoa(nomeAlterado, novoEmail, novoTel, novoCpf, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
                print('Cliente alterado com sucesso!')
            else:
                print("O cliete para o qual deseja alterar já existe!")
        else:
            print('Cliente que deseja alterar não está cadastrado no sistema!')
        with open('./arq/pessoas.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.email + '|' + i.telefone + '|' +
                            i.cpf + '|' + i.endereco)
                arq.writelines('\n')

    def mostrarClientes(self):
        x = PessoaDao.ler()
        if len(x) <= 0:
            print('Nenhum cliente cadastrado!')
        else:
            cont = 1
            total = 0
            for i in x:
                print(f"==========Cliente: {cont}==========")
                print(f'Cliente: {i.nome}\n'
                      f'Email: {i.email}\n'
                      f'Cpf: {i.cpf}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Endereço: {i.endereco}')
                cont += 1
                total += 1
            print('==============================')
            print(f'Total de clientes: {total}')

class ControllerVendedor:
    def cadastrarVendedor(self, nome, email, tel, cpf, endereco, clt):
        x = VendedorDao.ler()
        listarCpf = list(filter(lambda x: x.cpf == clt, x))
        listarClt = list(filter(lambda x: x.clt == clt, x))
        if len(listarCpf) > 0:
            print('Cpf já cadastrado!')
        elif len(listarClt) > 0:
            print('Clt já cadastrado!')
        else:
            if len(cpf) == 11 and len(tel) <= 11 and len(tel) >= 10:
                VendedorDao.salvar(Vendedor(nome, email, tel, cpf, endereco, clt))
                print('Vendedor cadastrado com sucesso!')
            else:
                print("Digite um cpf ou telefone válido!")

    def removerVendedor(self, delVendedor):
        x = VendedorDao.ler()
        vendedores = list(filter(lambda x: x.nome == delVendedor, x))
        if len(vendedores) == 0:
            print('O vendedor que deseja remover não existe!')
            return None #tenta apagar caso de ruim
        else:
            for i in range(len(x)):
                if x[i].nome == delVendedor:
                    del x[i]
                    print('Vendedor removido do sistema com sucesso!')
                    break                    
        with open('./arq/vendedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.email + '|' + i.telefone + '|' +
                           i.cpf + '|' + i.endereco + '|' + i.clt)
                arq.writelines('\n')

    def alterarVendedor(self, nomeAlterar, nomeAlterado, novoEmail, novoTel, novoCpf, novoEndereco, novoClt):
        x = VendedorDao.ler()
        if len(x) > 0:
            vendedores = list(filter(lambda x: x.nome == nomeAlterar, x))
            if len(vendedores) > 0:
                vendedores1 = list(filter(lambda x: x.nome == nomeAlterado, x))
                if len(vendedores1) == 0:
                    x = list(map(lambda x: Vendedor(nomeAlterado, novoEmail, novoTel, novoCpf, novoEndereco, novoClt) if (x.nome == nomeAlterar) else(x), x))
                    print('Dados do vendedor alterados com sucesso!')
                else:
                    print("O vendedor para o qual deseja alterar já existe!")
            else:
                print("O vendedor que deseja alterar não existe!")
        else:
            print('nenhum vendedor cadastrado!')
        with open('./arq/vendedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.email + '|' + i.telefone + '|' +
                           i.cpf + '|' + i.endereco + '|' + i.clt)
                arq.writelines('\n')

    def mostrarVendedores(self):
        x = VendedorDao.ler()
        if len(x) <= 0:
            print("Nenhum vendedor cadastrado!")
        else:
            cont = 1
            total = 0
            for i in x:
                print(f"==========Vendedor: {cont}==========")
                print(f'Vendedor: {i.nome}\n'
                      f'Email: {i.email}\n'
                      f'Cpf: {i.cpf}\n'
                      f'Telefone: {i.telefone}\n'
                      f'Endereço: {i.endereco}\n'
                      f'Clt: {i.clt}')
                cont += 1
                total += 1
            print('===============================')
            print(f'Total de vendedores: {total}')
