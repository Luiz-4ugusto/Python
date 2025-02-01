class Televisao:

    def __init__(self,canal,minimo=2 ,maximo=14):
        self.ligada = True
        self.canal = canal
        self.marca = 'LG'
        self.tamanho = 42
        self.minimo = 2
        self.maximo= 99

    def __str__(self):
        return (F"\n{'-'*50}\nTelevisão... \nMarca: " +
            self.marca + "\nTamnaho: %d" % self.tamanho + 
            "\nCanal: %d" % self.canal + "\nStatus: " + 
            (("A TV esta ligada" if self.ligada else "A tv não esta ligada")) +("\nCanal min: %d" % self.minimo) +("\nCanal max: %d" % self.maximo))


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

tv1= Televisao(canal=2)
tv1.retornar()
print(tv1)

tv2= Televisao(canal=11, minimo=4, maximo= 32)
tv2.avancar()
print(tv2)
