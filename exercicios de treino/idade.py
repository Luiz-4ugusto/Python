import random

idade = random.randint(1,100)
x1=idade
if idade<=13: 
    print(f'é uma crinça de {x1} anos')
elif idade>13 and idade<21:
    print(f'é um adolecente de {x1} anos')
elif idade>=21 and idade<60:
    print(f'é um adulto de {x1} anos')
else:
    print(f'é um idoso de {x1} anos')
