import random 

numeroale = [1,2,3]
NumeroRand =[1,2,3]

v1 = random.choice(numeroale)
v2 = random.choice(NumeroRand)

if v1<v2:
    print(f'valor 2 é maior, o valor 1 é {v1} e o valor 2 é {v2}')
elif v1>v2:
    print(f'valor 1 é maior, o valor 1 é {v1} e o valor 2 é {v2}')
elif v1==v2: 
    print(f'o resultado é empate e o novo resultado é')