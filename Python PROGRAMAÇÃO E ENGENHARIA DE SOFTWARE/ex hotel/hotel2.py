class hospede:

    def __init__(self, id, nome, endereco, tel,email):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.tel = tel
        self.email = email

    def __str__(self) -> str:
        return f"""
        {38*"-"}
       |          ==HOSPEDE==                        
       |Nome:{self.nome}                   
       |Endereço:{self.endereco}           
       |Tel:{self.tel}                     
       |Email:{self.email}                
        {38*"-"}"""

class reserva :

    def __init__(self, DE, DA, acompanhantes,nume_quarto):
        self.DE = DE
        self.DA  = DA 
        self.acompanhantes = acompanhantes
        self.nume_quarto= nume_quarto
        
    def __str__(self) -> str:
        return F"""
        {38*"-"}
       |            ==RESERVA==                        
       |Dia de entrada:{self.DE}           
       |Dia de saida:{self.DA}             
       |Acompanhantes:{self.acompanhantes} 
       |Numero do quarto:{self.nume_quarto}
        {38*"-"}"""
class quarto:

    def __init__(self, numero, tipo, quarto):
        self.numero = numero
        self.tipo  = tipo 
        self.quarto = quarto

    def __str__(self) -> str:
        return F"""
        {38*"-"}
       |            ==QUARTO==                        
       |Número:{self.numero}              
       |Tipo:{self.tipo}                  
       |O valor do quarto é:{self.quarto}
        {38*"-"}"""
class TIPO_QUARTO:

    def __init__(self, describition):
        self.describition=describition

    def __str__(self) -> str:
        return F"""
       {39*"-"}
       |            ==DESCRIÇÂO DO QUARTO==
       |o quarto possui:{self.describition}
       {39*"-"}
        """
class servico:

    def __init__(self, id_servico, nome_Ser, valor):
        self.id_servico = id_servico
        self.nome_Ser  = nome_Ser 
        self.valor = valor

    def __str__(self) -> str:
        return F"""
        {38*"-"}
       |            ==SERVIÇO==                        
       |Id:{self.id_servico}               
       |Serviço:{self.nome_Ser}            
       |Valor:{self.valor}                 
        {38*"-"}"""
class hospedagem (reserva):

    def __init__(self, DE, DA, acompanhantes, nume_quarto, modelo,placa):
        super().__init__(DE, DA, acompanhantes, nume_quarto)
        self.modelo=modelo
        self.placa=placa

    def __str__(self) -> str:
        return F"""
       {38*"-"}
       |            ==HOSPEDAGEM==                        
       |Dia de entrada:{self.DE}           
       |Dia de saida:{self.DA}             
       |Acompanhantes:{self.acompanhantes} 
       |Numero do quarto:{self.nume_quarto}
       |modelo do veiculo:{self.modelo}
       |placa do veiculo:{self.placa}
       {38*"-"}"""
    
class tipo_servico (servico):

    def __init__(self,  descricao):
        self.descricao=descricao

    def __str__(self) -> str:
        return F"""
       {38*"-"}
       |            ==DESCRIÇÃO DO SERVIÇO==                        
       |descrição:{self.descricao}
       {38*"-"}"""


        
cliente=hospede (1,"Austin" , "Rua", "(48)23213-3131", "email.com")
reservaa= reserva (10, 12, 1, 12)
locacao= quarto(3, "duplo" , 500)
servicos= servico (2, "comida", 12)
hospedagemm= hospedagem(10, 12, 1, 12,"não possui veiculo","não possui veiculo")
aaa=tipo_servico("levar comida")
bbb=TIPO_QUARTO("suite deluxe")
dias=reservaa.DA-reservaa.DE
total= locacao.quarto*dias+servicos.valor
AAAA= 12*" "
print(cliente)
print(locacao)
print(bbb)
print(reservaa)
print(servicos)
print(aaa)
print(hospedagemm)
print(F'{AAAA} {25*"-"}')
print(f"{AAAA}| o valor final é: {total}")
print(F'{AAAA} {25*"-"}')