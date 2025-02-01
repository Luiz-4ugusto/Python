from clientes import Cliente
from contas import Conta

joao = Cliente ("joão", "243-2354")
maria = Cliente ("Maria", "767-4782")
jose= Cliente ("jose", "767-4782")

conta1 = Conta([joao], 1, 100)
conta2 = Conta([joao, maria], 2, 500)
conta3 = Conta([joao, jose], 2, 500)



# conta1.saque(50)
# conta2.deposito(300)
# conta1.saque(190)
# conta2.deposito(95.15)
# conta2.saque(250)
# conta1.extrato()
# conta2.extrato()
# conta3.extrato()

# conta1.resumo()

# conta2.resumo()

# conta3.resumo()
