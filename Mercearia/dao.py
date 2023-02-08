from models import *

class CategoriaDao:
    @classmethod
    def salvar(cls, categoria):
        with open('./arq/categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('./arq/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat
    
class VendaDao:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('./arq/venda.txt', 'a') as arq:
            arq.writelines(venda.itemVendido.nome_p + "|" + venda.itemVendido.preco + "|" +
                           venda.itemVendido.categoria + "|" + venda.vendedor + "|" + venda.cliente + "|" +
                           str(venda.quantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('./arq/venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        sale = []
        for i in cls.venda:
            sale.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return sale

class EstoqueDao:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('./arq/estoque.txt', 'a') as arq:
            arq.writelines(produto.nome_p + '|' + produto.preco + '|' + 
                           produto.categoria + '|' + str(quantidade))
            
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('./arq/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
    
        stock = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                stock.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
            return stock
    
class FornecedorDao:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('./arq/fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome_f + '|' + fornecedor.cnpj + '|' + 
                           fornecedor.telefone + '|' + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('./arq/fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        provider = []
        for i in cls.fornecedor:
            provider.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return provider
    
class PessoaDao:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('./arq/pessoas.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.email + '|' + pessoas.telefone + '|' +
                           pessoas. cpf + '|' + pessoas.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('./arq/pessoas.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes
    
class VendedorDao:
    @classmethod
    def salvar(cls, vendedor: Vendedor):
        with open('./arq/vendedor.txt', 'a') as arq:
            arq.writelines(vendedor.nome + '|' + vendedor.email + '|' + vendedor.telefone + '|' +
                           vendedor.cpf + '|' + vendedor.endereco + '|' + vendedor.clt)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('./arq/vendedor.txt', 'r') as arq:
            cls.vendedores = arq.readlines()
        cls.vendedores = list(map(lambda x: x.replace('\n', ''), cls.vendedores))
        cls.vendedores = list(map(lambda x: x.split('|'), cls.vendedores))

        vendedor = []
        for i in cls.vendedores:
            vendedor.append(Vendedor(i[0], i[1], i[2], i[3], i[4], i[5]))
        return vendedor