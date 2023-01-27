from datetime import datetime

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.email =email
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco

class Cliente(Pessoa):
    def __init__(self, nome, telefone, cpf, email, endereco, id_cliente):
        super().__init__(nome, telefone, cpf, email, endereco)
        self.id_cliente = id_cliente

class Vendedor(Pessoa):
    def __init__(self, nome, telefone, cpf, email, endereco, clt):
        super().__init__(nome, telefone, cpf, email, endereco)
        self.clt = clt

#

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome_p, preco, categoria):
        self.nome_p = nome_p
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itemVendido: Produtos, vendedor, cliente, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itemVendido = itemVendido
        self.vendedor = vendedor
        self.cliente = cliente
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome_f, cnpj, telefone, categoria):
        self.nome_f = nome_f
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

