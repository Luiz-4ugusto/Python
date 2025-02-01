import time 
x = 0
num= input("pense em um numero ")
y = 0
a=0
while True:
    while x < 1: 
        x = x+1
        time.sleep(1) 
        print(f'tentando adivinhar seu numero')
    while y < 1: 
        y = y+1
        time.sleep(1) 
        print(f'aguarde..')   
    while a < 1: 
        a = a+1
        time.sleep(6) 
        print(f'o seu numero é {num}')
        break