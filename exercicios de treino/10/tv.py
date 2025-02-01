class Televisão: 
    def __init__ (self): 
        self.ligada = True 
        self.canal = 2 
        self.tamanho = 1041
        self.marca = "nokia"
tv1 = Televisão()  #criou objeto
tv2 = Televisão()
tv1.tamanho = 30
tv1.marca = "nokia"
tv2.tamanho = 15
tv2.marca = "ching ling"
tv2.canal
print(tv2.canal)

print(f'canal: {tv1.canal}, polegadas: {tv1.tamanho}", marca: {tv1.marca}')
print(f'canal: {tv2.canal}, polegadas: {tv2.tamanho}", marca: {tv2.marca}')

