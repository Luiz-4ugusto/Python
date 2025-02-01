genero=str(input("genero M masculino ou F feminino:")).upper()
alt=float(input("altura:"))

if genero == "M":
    peso_ideal= (72.7 * alt) - 58
    print(f"{peso_ideal:.2f}")
elif genero == "F":
    peso_ideal=(62.1 * alt) - 44.7
    print(f"{peso_ideal:.2f}")
else:
    print("error")
