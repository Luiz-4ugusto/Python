# 5. Escreva as seguintes funções:
# a) Crie um tipo de produto. Para isso use um dicionário. O produto deve ter as seguintes
# informações: nome, categoria e valor.
# b) Calcular o imposto sobre produtos de acordo com sua categoria (categoria 1 – 10%, categoria 2 –
# 20%, categoria 3 – 40%). A função recebe o produto, verifica a categoria
# Escreva um programa que crie uma lista de produtos (chamando a função (a)) e mostre na tela o a
# valor do imposto para cada produto.

def criar_produtos(nome, categoria, valor): 
    produto= {"nome":nome, "categoria": categoria, "valor": valor}
    return produto

produtos= list()

while True:
    opcao = str(input('Você que colocar um produto? ( S ou N ): ')).upper()
    if opcao == "S":
        nome= str(input("digite o nome"))
        categoria= int(input("digite a categoria"))
        valor= float(input("digite o valor"))
        produtos.append(criar_produtos(nome, categoria, valor))
    elif opcao == 'N':
        break
    else:
        print('Erro! Tente Novamente.')

def calcular_imposto(produto):
    categoria= produto['categoria']
    if categoria == 1:
        imposto= produto['valor']*0.1
    elif categoria == 2:
        imposto= produto['valor']*0.2
    elif categoria == 4:
        imposto= produto['valor']*0.4
    else:
        imposto=0
    return imposto

for produto in produtos:
    imposto = calcular_imposto(produto)
    print(f"{'-'*50}\n Nome: {produto['nome']}\n Categoria: {produto['categoria']}\n Valor: {produto['valor']}\n Seu imposto foi de: {imposto}")