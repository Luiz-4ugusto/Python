class pessoa:
    def __init__(self, nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    def envelher (self,envelher: int=0):
        self.envelher=envelher
        self.idade +=1
        self.envelher = self.idade
    def engoradar (self,engordar):
        self.engoradar =engordar
        self.peso += self.engoradar
    def emagrecer(self, emagrecer):
        self.emagrecer =emagrecer
        self.emagrecer =emagrecer
    def crescer(self):
        self.altura +=0,5
    def mostrar(self):
        print(f"{self.nome}, {self.idade}, {self.peso} , {self.altura}, {self.engoradar}, {self.emagrecer}, {self.envelher}")
valor= pessoa("joão", 12, 102, 132)
valor.engoradar (10)
valor.emagrecer (12)
valor.envelher (0)
valor.mostrar()


    #Métodos: Envelhercer, engordar, emagrecer, crescer. 
    # Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
    # sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.