# 1. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule
# seu peso ideal, utilizando as seguintes fórmulas:
# ● para homens: (72.7 * h) – 58;
# ● para mulheres: (62.1 * h) – 44.7.
sexo= str(input("se for mulher escreva M se for homem escreva H: "))
alt=float(input("what is your altura? "))
peso=float(input("what is your peso? "))
if sexo == "M" or sexo == "m":
    peso_ideal=(62.1 * alt) -44.7
    print(f'seu peso é {peso} e seu pesso ideal é {peso_ideal:.2f}')
elif sexo == "H" or sexo == "h":
    peso_ideal=(72.7 * alt)- 58
    print(f'seu peso é {peso} e seu pesso ideal é {peso_ideal:.2f}')
else:
    print("no sexo")