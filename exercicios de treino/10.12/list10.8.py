from cliente import Cliente
from conta import Conta

joao = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([joao], 1, 100)
conta2 = Conta([joao, maria], 2, 500)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190) #não permite pq o saldo ficaria negativo
conta2.deposito(95.15)
conta1.saque(250)#não permite pq o saldo ficaria negativo
conta1.extrato()
conta2.extrato()
