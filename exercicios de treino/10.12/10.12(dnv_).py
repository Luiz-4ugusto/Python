class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacao = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.numero} Saldo: {self.saldo:10.2f}")

    def pode_sacar(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacao.append(["SAQUE", valor])
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacao.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacao:
            print(f"{o[0]:10s}   {o[1]:10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor

    def extrato(self):
        Conta.extrato(self)
        print(f"\n     Limite: {self.limite:10.2f}\n")
        print(f"\n Disponivel: {self.limite + self.saldo:10.2f}\n")


jose = Cliente("Jose", "1243-3321")

conta = ContaEspecial([jose], 3432, 5000, 1000)
conta.extrato()
conta.saque(6000)
conta.saque(3000)
conta.saque(1000)
conta.extrato()