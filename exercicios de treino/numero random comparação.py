import random 

numeroale = list(range(1,100))
NumeroRand = list(range(1,100))

v1 = random.choice(numeroale)
v2 = random.choice(NumeroRand)

if v1 <v2:
    print("o valor 2 é maior e seu valor é",v2, "o primerio valor é",v1)
elif v1 == v2:
    print("o resultado é empate e o valor é",v1)
else:
    print("o valor 1 é maior e seu valor é",v1, "o segundo valor é",v2)

