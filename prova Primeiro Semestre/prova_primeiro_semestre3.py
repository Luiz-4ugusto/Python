arquivo = open("distância.txt", "w")
while True:
    origem = input("Digite a origem: ")
    destino = input("Digite o destino: ")
    km = input("Digite os km: ")
    arquivo.write(f"{origem},{destino},{km}\n")
    opcao = input("digite o 'C' se deseja parar o cadastro: ")

    if opcao.upper() == "C":
        break
  
arquivo.close()