A= float(input("qual o vaaalor de A no c"))
B= float(input("qual o valor de B no c"))
A1= float(input("qual o vaaalor de A no D"))
B1= float(input("qual o valor de B no D"))

while True:
    if A<10000:
        D= 1/2 * (3*A1-5*B1)
        C= 3*A- 3*B
        dc= D-C
        print (f"valor de {C}")
        print (f"valor de {D}")
        print (f"valor de {dc}")
        break
