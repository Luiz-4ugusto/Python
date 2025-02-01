protudos= ['carne','queijo','peixe','água gucci','arroz','feijão','batata','uva','goiaba','maracuja']
valor = ('100','5,99','20,40','10000','5,99','5','3,23','4','10','7')

item = input("digite oque deseja:" )

if item in protudos:

    id = int(protudos.index(item))
    end = valor [id]
    print(f'o item selecionado é {item} e seu valor é:  R${end}')
else: 
    print("não tem no nosso estoque")



