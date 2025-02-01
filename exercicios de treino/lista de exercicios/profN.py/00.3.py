# 3. Escreva um programa que faça um cadastro de clientes. Seu programa deve receber os seguintes
# dados do usuário: 1) o nome completo; 2) o RG do cliente; 3) o CPF e; 4) o telefone do cliente.
# [Processamento]: Seu programa deve armazenar todos os dados em uma ÚNICA LISTA. [Saída]:
# AO FINAL, SOMENTE AO FINAL, Seu programe deve mostrar (um cliente por linha): a) o nome
# completo do paciente, b) O RG; c) o CPF e; d) o telefone do cliente.
pessoas = []
pessoa = []
o= ""
while True:
    nome=str(input("nome:"))
    rg= int(input("rg:"))
    cpf=int(input("cpf:"))
    tel=int(input("telefone:"))
    pessoas.append([nome, rg, cpf, tel])
    choice= " "
    #opção fica vazio dessa maneira
    while choice not in ("S", "N"):
       choice= str(input("Quer continua S sim ou N não")).upper()
       if choice not in ("S", "N"):
           print("OPÇÃO INVALIDA, TENTE NOVAMENTE")
    if choice == "N":
        break
print(pessoas)
for pessoa in pessoas:
   print(f"{'-'*50}\n cadastro efetuado com sucesso! {o}\n{'-'*50}\n Nome:{pessoa[0]}\n Rg: {pessoa[1]}\n CPF: {pessoa[2]}\n telefone:{pessoa[3]}")
   