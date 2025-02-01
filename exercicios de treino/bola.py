class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.cor_original = cor
        self.circunferencia = circunferencia
        self.material = material
    def troca(self,nova_cor):
        nova_cor=str(input("qual cor?"))
        self.cor= nova_cor
    def mostra(self):
        print(self.cor)

bolinha= Bola("ciano", 2, "tijolo")
bolinha.troca("vermelho")
bolinha.mostra()