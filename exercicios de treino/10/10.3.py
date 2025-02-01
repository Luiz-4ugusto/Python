class Televisao:

    def __init__(self,canal):
        self.ligada = False
        self.canal = canal
        self.marca = 'LG'
        self.tamanho = 42
        self.minimo = 2
        self.maximo= 99

    def __str__(self):
        return (F"\n{'-'*50}\nTelevisão... \nMarca: " +
            self.marca + "\nTamnaho: %d" % self.tamanho + 
            "\nCanal: %d" % self.canal + "\nStatus: " + 
            (("A TV esta ligada" if self.ligada else "A tv não esta ligada")))

    def avancar(self):
        if self.canal == self.maximo:
            self.canal = self.minimo
        else:
            self.canal += 1
    def retornar(self):
       if self.canal == self.minimo:
            self.canal = self.maximo
       else:
            self.canal -= 1

channel= int(input("qual canal atual? "))
go= str(input("avançar A ou retornar R")).upper()
if go == "A":
    tv1 = Televisao(canal=channel)
    tv1.avancar()
    print(tv1)
else:
    tv1 = Televisao(canal=channel)
    tv1.retornar()
    print(tv1)

