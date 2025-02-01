lugar= input("digite se é  R-residência,  I-indústria ou para C-Comercial: ")
kmw= float(input("a quantidade de kWh consumida"))

if lugar == "R" :
    if kmw<=500:
        total= (kmw*0.40)
        print(total)
    else:
            total= (kmw*0.65)
            print(total)


if lugar == "I":
    if kmw<=1000:
        total= (kmw*0.55)
    print(total)
else:
    total= (kmw*0.60)
    print(total)

if lugar == "C":
    if kmw<=5000:
        total= (kmw*0.55)
    print(total)
else:
    total= (kmw*0.60)
print(total)

