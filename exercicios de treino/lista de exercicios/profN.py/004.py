# Escreva um programa que salve a lista de clientes do exercício anterior em um arquivo texto.
pessoas = []
pessoa = []

while True:
    nome=str(input("nome:"))
    rg= int(input("rg"))
    cpf=int(input("cpf"))
    tel=int(input("telefone"))
    pessoas.append([nome, rg, cpf, tel])
    opcao= " "
    #opção fica vazio dessa maneira
    while opcao not in ("S", "N"):
       opcao= str(input("Quer continua S sim ou N não")).upper()
       if opcao not in ("S", "N"):
           print("OPÇÃO INVALIDA, TENTE NOVAMENTE")
    if opcao == "N":
        break
print(pessoas)
#a adiciona no final do arquivo, parte da 4
with open(R"C:\Users\luiza\OneDrive\Área de Trabalho\codigos\profN.py\clientes.txt", "a") as arquivo:
    for pessoa in pessoas:
        arquivo.write(f"Nome: {pessoa[0]} Rg {pessoa[1]} CPF {pessoa[2]} telefone {pessoa[3]}\n")
with open(R"C:\Users\luiza\OneDrive\Área de Trabalho\codigos\profN.py\clientes.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
        print(pessoas)
       