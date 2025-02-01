class Partido:
    def __init__(self, codigo, sigla, nome):
        self.codigo = codigo
        self.sigla = sigla
        self.nome = nome
        self.votos = 0
        
    def __str__(self):
        result = (f"\n{self.codigo}\n{self.nome}" + 
            f"\n{self.sigla}\n{self.votos}")
        return result     