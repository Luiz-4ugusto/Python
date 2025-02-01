class Hospede:

    def __init__(self, id, nome, endereco, email):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return f"""
        ===tq=== Hóspede ======
        id: {self.id}
        nome: {self.nome}
        endereço: {self.endereco}
        email: {self.email}
        ====== ======= ======
        """

class TipoQuarto:

    def __init__(self, id, descricao, capacidade, valor_diaria):
        self.id = id
        self.descricao = descricao
        self.capacidade = capacidade
        self.valor_diaria = valor_diaria

    def __str__(self):
        return f"""
        ====== Tipo de Quarto ======
        id: {self.id}
        descrição: {self.descricao}
        capacidade: {self.capacidade}
        valor da diária: {self.valor_diaria}
        ====== =============== ======
        """    

class Quarto:

    def __init__(self, id, numero, tipo):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = tipo.valor_diaria

    def __str__(self):
                return f"""
        ====== Quarto ======
        id: {self.id}
        numero: {self.numero}
        tipo: {self.tipo.descricao}
        valor da diária: {self.valor_diaria}
        ====== Quarto ======
        """


class TipoServico:

    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor
    
    def __str__(self):
        return f"""
        ====== Tipo de Serviço ======
        id: {self.id}
        descrição: {self.descricao}
        valor: {self.valor}
        ====== =============== ======
        """

class Reserva:

    def __init__(self, id, hospede, data_chegada,
        data_saida, num_acompanhantes, tipo, situacao):
        self.id = id
        self.hospede = hospede
        self.data_chegada = data_chegada
        self.data_saida = data_saida
        self.num_acompanhantes = num_acompanhantes
        self.tipo_quarto = tipo
        self.situacao = situacao

    def __str__(self):
        return f"""
        ====== Reserva ======
        id: {self.id}
        hóspede: {self.hospede.nome}
        data chegada: {self.data_chegada}
        data saída: {self.data_saida}
        número de acompanhantes: {self.num_acompanhantes}
        tipo de quarto: {self.tipo_quarto}
        situação: {self.situacao}
        ====== =============== ======
        """    

class Servico:
    
    def __init__(self, id, tipo, data_pedido, 
        quantidade, desconto):
        self.id = id
        self.tipo_servico = tipo
        self.data_pedido = data_pedido
        self.quantidade = quantidade
        self.desconto = desconto

    def valor_total(self):
        return (self.quantidade *
             self.tipo_servico.valor *
             (1 - self.desconto / 100))

    def __str__(self):
        return f"""
        ====== Serviço ======
        id: {self.id}
        tipo de serviço: {self.tipo_servico}
        quantidade: {self.quantidade}
        data pedido: {self.data_pedido}
        desconto: {self.desconto}
        valor total: {self.vavalor_totlor_total()}   
        ====== =============== ======
        """
        

class Hospedagem:

    def __init__(self, id, placa_veiculo, reserva, diarias,
        quarto, modelo_veiculo, hospedes=[], servicos=[]):
        self.id = id
        self.placa_veiculo = placa_veiculo
        self.modelo_veiculo = modelo_veiculo
        self.reserva = reserva
        self.quarto = quarto
        self.diarias = diarias
        self.hospedes = hospedes
        self.servicos = servicos

    def valor_total(self):
        valor_diarias = self.diarias * self.quarto.valor_diaria
        total_servicos = 0
        for servico in self.servicos:
            total_servicos += servico.valor_total()
        return (valor_diarias + total_servicos)

    def __str__(self):
        return f"""
        ====== Hospedagem ======
        id: {self.id}
        hóspedes: {[h.nome for h in self.hospedes]}
        modelo do veículo: {self.modelo_veiculo}
        placa do veículo: {self.placa_veiculo}
        reserva: {self.reserva.id}
        quarto: {self.quarto.numero}
        diarias: {self.diarias}
        serviços: {[s.tipo_servico.descricao for s in self.servicos]}
        valor total: {self.valor_total()}   
        ====== =============== ======
        """




h1 = Hospede(1, "Bob", "Imbituba", "bob@email.com")
tq = TipoQuarto(1, "Suíte luxo", 4, 500)
q1 = Quarto(1, "202A", tq)
ts1 = TipoServico(1, "Lanche - Hamburger SuperFat", 30)
ts2 = TipoServico(2, "Barba/Cabelo - Corte Hipster", 50)
s1 = Servico(1, ts1, '2023-8-18', 2, 20)
s2 = Servico(2, ts2, '2023-8-28', 1, 0)

reserva = Reserva(1, h1, '2023-8-15','2023-8-18', 
            2, tq, 'Aberta')
hospedagem = Hospedagem(1,'MFV6686', reserva, 3, q1, 
                        'Honda Civic', [h1], [s1, s2])

print(hospedagem)

f=open("arquivo.txt","w") 
f.write(str(hospedagem)) 
f.close()