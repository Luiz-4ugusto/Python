import datetime


data=datetime.datetime.now()#fala a data atual

nascimento=datetime.datetime (2006,9,29) #só funciona na ordem ano,mes data


print (str(data.day) + "/" + str(data.month) + "/"+ str(data.year))#tem como colocar só print (data) mas assim fica mais bonito


print(nascimento)  #colocar o que ta no nascimento
#print(nascimento.strftime("%A")) fala semana de nasc 
#print(nascimento.strftime("%a")) dia semana resumido sunday vira sun
#print(nascimento.strftime("%w")) numero do dia da semana seguna = 1
#print(nascimento.strftime("%d")) dia do mês
#print(nascimento.strftime("%b")) mês abreviado
#print(nascimento.strftime("%B")) mês não abreviado
#print(nascimento.strftime("%m")) numero do mês
#print(nascimento.strftime("%y")) ano com dois digitos 
#print(nascimento.strftime("%Y")) ano com dois digitos 
#print(nascimento.strftime("%H")) 00-23 horas
#print(nascimento.strftime("%H")) 00-12 horas
#print(nascimento.strftime("%M")) minutos
#print(nascimento.strftime("%S")) segundos
#print(nascimento.strftime("%F")) microsegudos
#print(nascimento.strftime("%j")) dia do ano 365
#print(nascimento.strftime("%W")) numero da semana do ano
