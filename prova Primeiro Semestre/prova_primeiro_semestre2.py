from random import randint
num_ale= randint(1,11)
total=0
while True:
    chute= int(input("cute um numero ae"))
    total +=1
    if chute == num_ale:
        money = 100/total
        print(f"premio {money}")
        break
    else:
        print("tente novamente")