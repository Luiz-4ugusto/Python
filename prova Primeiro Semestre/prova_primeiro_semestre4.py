origem = input("digite a origem: ")
destino = input("digite o destino: ")
arquivo = open("distância.txt", "r")

for linha in arquivo:
    a = linha.split(",")
    a = linha.split(",")
    a = linha.split(",")

    if (origem in linha) and (destino in linha):
        print(f"A distância entre {a[0]} e {a[1]} é {a[2]}")
    else:
        print("Não tem no banco de dados")