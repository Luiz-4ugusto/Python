nome = input ("qual seu nome?: ")
salario= int (input( " qual o seu salario?: "))

if salario > 1000: 
    novoS = salario*(20/100) + salario
else:
    novoS = salario*(30/100) + salario

print (nome,"seu salario é", novoS ) 


