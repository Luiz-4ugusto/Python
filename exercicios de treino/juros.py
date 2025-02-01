
principal =  input ("qual foi o valor retirado: ")
meses= int (input( "quantidade de meses: "))
taxa =  (input("qual a taxa : "))

taxa1= taxa/100
    
montante = principal*pow((1+taxa1),meses)
juros = montante - principal
  
print("O total de juros a ser pago é:", juros)
print("O montante a ser pago é:", montante) 

