class Apuracao():
    def __init__(self):
        self.partidos = []
        self.candidatos = []

    def inclui_candidato(self,candidato):
        candidatoExiste = False
        for c in self.candidatos:
            if c.codigo == candidato.codigo:
                c.votos += candidato.votos
                candidatoExiste = True
                break
        if not candidatoExiste:
            self.candidatos.append(candidato)

        partidoExiste = False
        for p in self.partidos:
            if p.codigo == candidato.partido.codigo:
                p.votos += candidato.votos
                partidoExiste = True
                break
        if not partidoExiste:
            candidato.partido.votos = candidato.votos
            self.partidos.append(candidato.partido)

    #total de votos (eleitores que votaram)
    def total_votos(self):
        soma = 0
        for p in self.partidos:
            soma += p.votos
        return soma

    #partido mais votado
    def partido_mais_votado(self):
        if len(self.partidos) == 0:
            return None
        mais_votado = self.partidos[0]

        for p in self.partidos:
            if p.votos > mais_votado.votos:
                mais_votado = p
        return mais_votado

    #candidato mais votado
    def candidato_mais_votado(self):
        if len(self.candidatos) == 0:
            return None
        mais_votado = self.candidatos[0]
        for c in self.candidatos:
            if c.votos > mais_votado.votos:
                mais_votado = c
        return mais_votado

    #Str: retorna todas as informações da apuração
    def __str__(self):
        print("-"*50)
        result = f"\nTotal de votos: {self.total_votos()}"
        
        result += f"\nPartido mais votado: {self.partido_mais_votado()}"
        
        result += f"\nCandidato mais votado: {self.candidato_mais_votado()}"
        
        return result
        


        

