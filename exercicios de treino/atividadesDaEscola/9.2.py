arquivo=open("números.txt","w") 
ultimo= int(input("qual o ultimo digito da linha?"))
primeiro= int(input("qual o primeiro digito da linha?"))
ultimo += 1
for linha in range(primeiro,ultimo): 
 arquivo.write("%d\n" % linha) 
arquivo.close()
#Exercício 9.2 Modifique o programa do exercício 9.1 para que receba mais dois
#parâmetros: a linha de início e a de fim para impressão. O programa deve imprimir
#apenas as linhas entre esses dois valores (incluindo as linhas de início e fim)
# arquivo=open("números.txt","w") 
# for linha in range(1,5+1): 
#  arquivo.write("%d\n" % linha) 
# arquivo.close()
