from cliente import Cliente
from conta import Conta

joao = Cliente ("joão", "243-2354")
maria = Cliente ("Maria", "767-4782")

conta1 = Conta([joao], 1, 1000)
conta2 = Conta([joao, maria], 2, 500)
conta1.saque(50)
conta2.saque(300)
conta1.resumo()
conta2.resumo()

