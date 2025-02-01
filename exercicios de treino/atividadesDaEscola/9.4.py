numeroale = range(1,100+1)
NumeroRand =range(101,200+1)
tudo=open("tudo.txt","w")
v1=open("v1.txt","w")
v2=open("v2.txt","w")

for linha in numeroale: 
 v1.write("%d\n" % linha) 
 tudo.write("%d\n" % linha)


for linha in NumeroRand: 
 v2.write("%d\n" % linha) 
 tudo.write("%d\n" % linha)
v2.close()
v1.close()
tudo.close()
# Exercício 9.4 Crie um programa que receba o nome de dois arquivos como pa-
# râmetros da linha de comando e que gere um arquivo de saída com as linhas do
# primeiro e do segundo arquivo.