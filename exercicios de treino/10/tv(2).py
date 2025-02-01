class Televisao:
    def __init__ (self, canal):
        self.ligado = True
        self.canal = canal

canal = int(input("qual canal"))

tv1 = Televisao(canal)

print(f'canal {tv1.canal}')