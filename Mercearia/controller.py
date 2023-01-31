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
a = ControllerEstoque()
a.alterarProduto('uva', 'laranja', '22', 'Frutas', 450)