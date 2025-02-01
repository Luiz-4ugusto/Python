from clientes import Cliente
from contas import Conta, ContaEspecial

joao = Cliente ("joão", "243-2354")
maria = Cliente ("Maria", "767-4782")

conta1 = Conta([joao], 1, 1000)
conta2 = ContaEspecial([joao, maria], 2, 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()

