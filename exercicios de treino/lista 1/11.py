# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# .o produto do dobro do primeiro com metade do segundo é
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
v1=int(input("v1? "))
v2=int(input("v2? "))
v3=float(input("v3? "))
a=(v1*2)/(v2/2)
b=(v1*3)+v3
c=v3**3
print(f'o produto do dobro do primeiro com metade do segundo é {a:.2f}')
print(f' a soma do triplo do primeiro com o terceiro é {b:.2f}')
print(f' o terceiro elevado ao cubo{c:.2f}')