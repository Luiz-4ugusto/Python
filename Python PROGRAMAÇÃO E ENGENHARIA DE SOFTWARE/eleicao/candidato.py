class Candidato:
    def __init__(self, codigo, nome, partido, votos):
        self.codigo = codigo
        self.nome = nome
        self.partido = partido
        self.votos = votos

    def __str__(self):
        result = (f"\n{self.codigo}\n{self.nome}" + 
            f"\n{self.partido.nome}\n{self.votos}")
        return result