class C_Veiculo:
    def __init__(self, placa, marca, modelo, ano , valor_locacoes):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano =  ano
        self.valor_locacoes =  valor_locacoes


class C_Nao_Motorizados(C_Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_locacoes):
        super().__init__(placa, marca, modelo, ano, valor_locacoes)


class C_motorizados(C_Veiculo):
    def __init__(self, placa, marca, modelo, ano, valor_locacoes,km, potencia):
        super().__init__(placa, marca, modelo, ano, valor_locacoes)
        self.km=km
        self.potencia=potencia

class C_Locacoes:

    def __init__(self, dia, desconto):
        self.desconto = desconto
        self.dia = dia
class C_LOCACOES_MOTOZIDAS(C_Locacoes):
    def __init__(self, dia, desconto,taxa,km_percorrido):
        super().__init__(dia, desconto)
        self.taxa= taxa
        self.km_percorrido= km_percorrido
    def L_nao_motorizados (self, diaria):
            self.diaria= diaria
    def L_motorizados (self, diaria, taxa_km):
        self.diaria = diaria
        self.taxa_km = taxa_km