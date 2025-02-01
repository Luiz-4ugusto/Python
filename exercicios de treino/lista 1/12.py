#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58
a=float(input("what is your altura? "))
p=float(input("what is your peso ideal? "))
peso=(72.7*a) - 58
if peso>=p:
    print(f'pesso não ideal, {p} e seu peço é {peso}')
else:
    print(f'pesso ideal, {p} e seu peço é {peso}')