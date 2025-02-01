class veiculos:
    def __init__(self, motorizados, nao_motorizados):
        self.motorizados = motorizados
        self.nao_motorizados = nao_motorizados

    def nao_motorizados (self, placa, marca, modelo, ano , valor_locacoes):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano =  ano
        self.valor_locacoes =  valor_locacoes
    def motorizados (self, km, potencia):
        self.km = km
        self.potencia = potencia

class locacoes:

    def __init__(self, dia, desconto):
        self.desconto = desconto
        self.dia = dia

    def L_nao_motorizados (self, diaria):
            self.diaria= diaria
    def L_motorizados (self, diaria, taxa_km):
        self.diaria = diaria
        self.taxa_km = taxa_km

        fazer outro def que vai fazer a conta 1000*km




class aplicacao:


        

