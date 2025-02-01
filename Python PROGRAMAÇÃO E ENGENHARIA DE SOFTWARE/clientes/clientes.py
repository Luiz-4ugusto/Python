class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return ("\nCliente:" + self.nome + "\nTelefone: " + self.telefone)

joao = Cliente ("joão", "243-2354")
maria = Cliente ("Maria", "767-4782")
jose= Cliente ("Maria", "767-4782")
print(joao)
print(maria)
print(jose)
