class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = 'LG'
        self.tamanho = 42


    def __str__(self):
        return (F"\n{'-'*50}\nTelevisão... \nMarca: " +
            self.marca + "\nTamnaho: %d" % self.tamanho + 
            "\nCanal: %d" % self.canal + "\nStatus: " + 
            (("A TV esta ligada" if self.ligada else "A tv não esta ligada")))
 
tv1 = Televisao()
print(tv1)