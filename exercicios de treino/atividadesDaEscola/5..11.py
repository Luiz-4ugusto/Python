taxa= float(input("qual valor da taxxa: "))
deposito= float(input("qual valor do deposito: "))
mes=1
saldo=deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa/100))
    print(f"Saldo do mês {mes} é de R${saldo}.")
    mes = mes + 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito}.")