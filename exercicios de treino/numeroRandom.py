import random 

numeroale = range(1,100)
NumeroRand =range(1,100)

v1 = random.choice(numeroale)
v2 = random.choice(NumeroRand)

if v1 <v2:
    print(f'o v2 é maior {v2} e o outro é {v1}')
elif v1 == v2:
    print(f'o resultado é empate {v1}')
elif v2<v1:
    print(f'v1 é o maior {v1} e o outro é {v2}')

