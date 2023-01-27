from models import *

class CategoriaDao:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('./arq/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        print(cls.categoria)

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
        print(cls.venda)

        sale = []
        for i in cls.venda:
            sale.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return sale

VendaDao.ler()

 
    #classmethod
    #def vender(cls, itemVendido, vendedor, cliente, quantidadeVendida, data)
        #with open('venda.txt', 'a') as arq:
            #arq.writelines()