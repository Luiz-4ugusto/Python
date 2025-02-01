A = input ("qual o valor do lado A: ")
B = input ("qual o valor do lado B: ")
C = input ("qual o valor do lado C: ")

if  A == B and B==C:
    print(f'o triangulo é equilátero o valor dos lados A,B e C são {A}')
    
elif A != B and B!=C and A!=C:
    print(f'o triangulo é escaleno, o valor do lado A é {A}, o valor do lado B é {B} e o valor do C é {C}')

elif A == B and A != C:
    print(f'o triangulo é isósceles e A e B são iguais, seu valor é {A}, e são diferentes de C que é {C}')
elif C == B and C != A:
    print(f'o triangulo é isósceles e B e C são iguais, seu valor é {C}, e são diferentes de A que é {A}')
elif A == C and A != B:
    print(f'o triangulo é isósceles e A e C são iguais, seu valor é {C}, e são diferentes de B que é {B}')


