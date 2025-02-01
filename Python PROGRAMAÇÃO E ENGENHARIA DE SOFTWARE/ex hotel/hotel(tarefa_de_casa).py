class hospede:
    def __init__(self, id, nome, endereco, tel,email):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.tel = tel
        self.email = email
    def __str__(self) -> str:
        return f"""
        {50*"-"}
       |==HOSPEDE==                        
       |Nome:{self.nome}                   
       |Endereço:{self.endereco}           
       |Tel:{self.tel}                     
       |Email:{self.email}                
        {50*"-"}"""

class reserva :
    def __init__(self, DE, DA, acompanhantes,nume_quarto):
        self.DE = DE
        self.DA  = DA 
        self.acompanhantes = acompanhantes
        self.nume_quarto= nume_quarto
        
    def __str__(self) -> str:
        return F"""
        {50*"-"}
       |==RESERVA==                        
       |Dia de entrada:{self.DE}           
       |Dia de saida:{self.DA}             
       |Acompanhantes:{self.acompanhantes} 
       |Numero do quarto:{self.nume_quarto}
        {50*"-"}"""
class quarto:
    def __init__(self, numero, tipo, quarto):
        self.numero = numero
        self.tipo  = tipo 
        self.quarto = quarto
    def __str__(self) -> str:
        return F"""
        {50*"-"}
       |==QUARTO==                        
       |Número:{self.numero}              
       |Tipo:{self.tipo}                  
       |Quarto:{self.quarto}
        {50*"-"}"""
class servico:
    def __init__(self, id_servico, nome_Ser, valor):
        self.id_servico = id_servico
        self.nome_Ser  = nome_Ser 
        self.valor = valor
    def __str__(self) -> str:
        return F"""
        {50*"-"}
       |==SERVIÇO==                        
       |Id:{self.id_servico}               
       |Serviço:{self.nome_Ser}            
       |Valor:{self.valor}                 
        {50*"-"}"""
class hospedagem (reserva):
    def __init__(self, DE, DA, acompanhantes, nume_quarto, modelo,placa):
        super().__init__(DE, DA, acompanhantes, nume_quarto)
        self.modelo=modelo
        self.placa=placa
    def __str__(self) -> str:
        return F"""
       {50*"-"}
       |==hospedagem==                        
       |Dia de entrada:{self.DE}           
       |Dia de saida:{self.DA}             
       |Acompanhantes:{self.acompanhantes} 
       |Numero do quarto:{self.nume_quarto}
       |modelo do veiculo:{self.modelo}
       |placa do veiculo:{self.placa}
       {50*"-"}"""


        
cliente=hospede (1,"Austin" , "Rua", "(48)23213-3131", "email.com")
reservaa= reserva (10, 12, 1, 12)
locacao= quarto(3, "duplo" , 12)
servicos= servico (2, "comida", 12)
hospedagemm= hospedagem(10, 12, 1, 12,"não possui veiculo","não possui veiculo")
dias=reservaa.DA-reservaa.DE
total= locacao.quarto*dias+servicos.valor
print(cliente)
print(locacao)
print(reservaa)
print(servicos)
print(hospedagemm)
print((20*"-"))
print(f"o valor final é: {total}")
print(20*"-")



