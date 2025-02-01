class Estado:
    def __init__(self, nome, sigla, cidades=[]):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def __str__(self):
        result = ("\nEstado: " + self.nome + "\tSigla: " + self.sigla)
        soma = 0
        for cidade in self.cidades:
            result += ("\n\tCidade:" + cidade.nome + "\tPopulação: %d" %
                cidade.populacao)
            soma += cidade.populacao

        result += "\nPopulação total: %d" % soma
        return result

            
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao


c1 = Cidade("Garopaba", 30000)
c2 = Cidade("Florianopolis", 530000)
c3 = Cidade("Imbituba", 50000)
estado = Estado("Santa Catarina", "SC", [c1, c2, c3])
estado.cidades.append(Cidade("Paulo Lopes", 9000))
print(estado)

    