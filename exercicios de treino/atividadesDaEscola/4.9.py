casaValor= int(input("valor da casa; "))
salario= int(input("valor do salario; "))
anosPagar= int(input("anos a pagar; "))
meses= anosPagar*12
prestacao= casaValor/meses
por= salario*0.3

if prestacao>por:
    print("negado")
else:
        print("sim")
