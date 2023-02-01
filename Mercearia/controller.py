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
            #TODO: COLCAR SEM CATEGORIA NO ESTOQUE
            with open('./arq/categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
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

    def mostrarCategoria(self):
        categorias = CategoriaDao.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        if len(categorias) > 0:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome_p, preco, categoria, quantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        stock = list(filter(lambda x: x.produto.nome_p == nome_p, x))
        
        if len(h) > 0:
            if len(stock) == 0:
                produto = Produtos(nome_p, preco, categoria)
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
                    if i.quantidade >= quantidadeVendida:
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


#a = ControllerVenda()
#a.cadastrarVenda('uva', 'Enzo', 'Danillo', 2)
c = ControllerVenda()
c.relatorioProdutos()
#b = ControllerEstoque()
#b.cadastrarProduto('banana', '5', 'Frutas', 250)