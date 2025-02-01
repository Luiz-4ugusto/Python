# pede ao usuário para fornecer informações sobre o investimento
valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (em porcentagem): "))
tempo = int(input("Digite o número de anos do investimento: "))

# converte a taxa de juros anual para uma taxa de juros mensal
taxa_juros_mensal = taxa_juros_anual / 12 / 100

# inicializa o valor futuro do investimento
valor_futuro = valor_inicial

# inicializa o contador de meses
mes = 0

# loop para calcular o valor futuro do investimento a cada mês
while mes < tempo * 12:
    # pede ao usuário para fornecer o valor do depósito mensal do mês
    valor_deposito_mensal = float(input(f"Digite o valor do depósito mensal do mês {mes+1}: "))
    # adiciona o valor depositado mensalmente ao valor futuro do investimento
    valor_futuro += valor_deposito_mensal
    # adiciona o juros ao valor futuro do investimento
    valor_futuro *= 1 + taxa_juros_mensal
    # incrementa o contador de meses
    mes += 1

# exibe o valor futuro do investimento
print(f"O valor futuro do investimento é de R${valor_futuro-valor_inicial:.2f}.")
