dia= int(input("quandos cicarros por dias"))
ano = int(input("quantos cicarros por ano?"))

quantidadeAno= (dia*365)*ano
vidaF= quantidadeAno*10
dias2 = (vidaF/60)/24
print(f'o tempo de vida perdido foi {dias2} e fumou por {vidaF}')