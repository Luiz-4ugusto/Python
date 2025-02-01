dias = int(input("quantos dias você esta nesse PC?"))
hora = int(input("quantos horas você esta nesse PC?"))
minuto = int(input("quantos minutos você esta nesse PC?"))
segundo = int(input("quantos segundos você esta nesse PC?"))
totais=0
totais += (dias*86400) + (hora*3600) + (minuto *60) + segundo
print(totais)