class TV:

    def __init__(self,canal,minimo=2 ,maximo=14):
        self.ligada = False
        self.canal = canal
        self.minimo = 2
        self.maximo= 3
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

    ligar= str(input("deseja ligar a TV? S caso queira N para não")).upper()
    while True:
        if ligar =="N":
            print("não po beleza.")
            break
        if ligar == "S":
            def __init__(self,canal,minimo=2 ,maximo=14):
                self.ligada = True
                self.canal = canal
                self.minimo = 2
                self.maximo= 3
            choice= int(input("qual canal do 1 ao 3 desejar ir?"))
            if choice ==1:
                print("Frezaaaaa porque você matou o kuririn, eu estou nervoso. Fique atendo ao proximo episodio Frezza morre, oque sera que ra acontecer?")
                break
            elif choice ==2:
                print("correr veloz com as mãos para trás, quem é o meu pai eu queria só saber, hogake eu quero serrr")
                break
            else:
                print("pokemon")
                break
si_no=str(input("desejar continuar? S caso queira N para não")).upper()
if si_no=="N":
    print("ok")
    
if si_no=="S":
    print("ok")
    channel= int(input("qual canal atual? "))
    go= str(input("avançar A ou retornar R")).upper()
if go == "A":
    tv1 = TV (canal=channel)
    tv1.avancar()
    print(tv1)
else:
    tv1 = TV (canal=channel)
    tv1.retornar()
    print(tv1)
    
