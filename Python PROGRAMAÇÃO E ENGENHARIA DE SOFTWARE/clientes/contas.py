class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacao=[]
    
    def resumo(self):
        print("CC número: %s \tSaldo: %10.2f" %
            (self.numero, self.saldo))
        
        for cliente in self.clientes:
            print("\nCliente: ", cliente.nome, "\ntelefone: ",cliente.telefone)
            print(f"{'-'*50}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacao.append(["SAQUE: ",valor])
        else:
            print("\nSaldo de %.2f é insuficiente para um saque de %.2f!" %
            (self.saldo, valor))
            print(f"{'-'*50}")

    def deposito(self, valor):
        self.saldo += valor
        self.operacao.append(["DEPOSITO: ",valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.numero)
        for o in self.operacao:
            print("%10s %10.2f" % (o[0],o[1]))
        print("\n Saldo: %10.2f\n" % self.saldo)
        print(f"{'-'*50}")

class ContaEspecial(Conta):
    def __init__( self , clientes, numero, saldo = 0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    def saque( self, valor):
        if self .saldo + self .limite >=valor:
            self. saldo -=valor
            self .operacao.append(["SAQUE", valor])