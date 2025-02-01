temp=str(input("coloque o valor em celcius ou fahrenheit"))
ultimo=len(temp)-1
escala=temp[ultimo]
temp= float(temp[:ultimo])
if escala.upper() == "C":
    f=(temp*1.8)+32
    print(f"o seu valor em fahrenheit é {f:.2f}F")
elif escala.upper()== "F":
    c=(temp-32)/1.8
    print(f"o seu valor em celcius é {c:.2f}C")
else: 
    print("valor invalido")