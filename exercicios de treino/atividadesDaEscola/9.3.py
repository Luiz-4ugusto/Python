tudo=open("tudo.txt","w")
impares=open("ímpares.txt","w")
pares=open("pares.txt","w")
for n in range(1,11):
    tudo.write("%d\n" % n) 
    if n % 2 == 0:		
        pares.write("%d\n" % n)
    else:
        impares.write("%d\n" % n)
impares.close()
pares.close()
tudo.close()
    # Exercício 9.3 Crie um programa que leia os arquivos pares.txt e ímpares.txt e que
# crie um só arquivo par ese impares.txt com todas as linhas dos outros dois arquivos,
# de forma a preservar a ordem numérica.