class macaco:
    def __init__(self, nome):
        self.nome =nome
        self.bucho=[]
    
        
    def comer(self,comer):
        self.bucho.append (comer)
    def Vbucho(self):
        print(f"ver o bucho do {self.nome}, ele comeu {self.bucho}")
    def digerir(self):
        self.bucho.clear()

    
macaco1 = macaco('monkey number one')
macaco2 = macaco('the other')


macaco1.comer('Banana')
macaco1.comer('tijolo')
macaco1.comer('aquilo')
macaco1.Vbucho()
macaco1.digerir()
macaco1.Vbucho()

macaco2.comer('Banana')
macaco2.comer('tijolo')
macaco2.comer('aquilo')
macaco2.Vbucho()
macaco2.digerir()
macaco2.Vbucho()
        # métodos comer(), verBucho() e digerir(). Faça um programa ou teste
        #interativamente, criando pelo menos dois macacos, 
        #alimentando-os com pelo menos 3 alimentos diferentes e verificando o 
        #conteúdo do estomago a cada refeição. Experimente fazer com que um macaco
        #coma o outro. É possível criar um macaco canibal?

