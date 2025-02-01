# Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a
# quantidade de números pares e ímpares, a média de valores pares e a média geral dos números
# lidos. O número que encerrará a leitura será zero.

impar=0
par=0
media=0
cont=0
medpar=0
while True:
    num = float(input("digite um numero maior ou igual a 0"))
    if num == 0:
     print(impar)
     print (par)
     print(medpar/par)
     print(media/cont)
     break

    if num % 2:
        impar += 1
        media += num
        cont += 1
    else:
        par += 1
        medpar += num
        cont+= 1