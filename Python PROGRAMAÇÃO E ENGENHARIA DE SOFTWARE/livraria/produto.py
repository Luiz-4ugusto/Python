class C_Produto:
    def __init__(self, codigo, descricao, autor, preco,quantidade_estoque):
        self.codigo = codigo
        self.descricao = descricao
        self.autor = autor
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

        #todas as classe vão receber essas descrições por herança, ou seja todas aquui

class C_Livro(C_Produto):
    def __init__(self, codigo, descricao, autor, preco, quantidade_estoque, ISBN):
        super().__init__(codigo, descricao, autor, preco, quantidade_estoque)
        self.ISBN = ISBN

class C_CD(C_Produto):
    def __init__(self, codigo, descricao, autor, preco, quantidade_estoque,N_faixas):
        super().__init__(codigo, descricao, autor, preco, quantidade_estoque)
        self.N_faixas = N_faixas

class C_ITEM:
    def __init__(self, quantidade, desconto,produto):
        self.quantidade = quantidade
        self.desconto = desconto
        self.produto= produto


class C_Venda:
    def __init__(self)->None: #'->None' quando rodar não vai retornar nada
        self.item= []

    def adicionar_item (self,item):
        if item not in self.item:
            self.item.append(item)


    def desconto(self):
        valor_produto=0
        for i in self.iten:
            valor_produto += ((i.desconto/100)*(i.produto.preco))

    def total (self):
        total = 0
        for i in self.item:
            total += i.produto.preco
            total -= ((i.desconto/100)* ((i.produto.preco) * i.quantidade))
        return total

    def nota (self):
        for i in self.item:
            print(f'\n Nome:{i.produto.descricao} \n Preço:R${i.produto.preco}\n Quantidade em estoque:{i.quantidade}')

        print(f'\ntotal:R${self.total():.2f}')

cd1= C_CD(2,'Xuxa','xuxa', 21.00, 4, 4)
cd2= C_CD(3,'Noite em Uruguai', 'D.Pedro2', 21.00, 4, 4)
l1= C_Livro(2,'Mil e 1 henriques', 'henrique', 21.00, 4, 4)
l2= C_Livro(3,'Varios continho e meio conto', 'legal', 21.00, 4, 4 )


i1=C_ITEM (7, 0, cd1)
i2=C_ITEM (3, 3, cd2)
i3=C_ITEM (2, 2, l1)
i4=C_ITEM (1, 4, l2)

v1= C_Venda()
v1.adicionar_item(i1)
v1.adicionar_item(i2)
v1.adicionar_item(i3)
v1.adicionar_item(i4)

v1.nota()