def registros():
    transacoes = int(input('Informe quantas transações realizou hoje: '))
    total_gasto = 0.0
    for x in range(1, transacoes+1):
        valo_gasto = float(input(f'Digite o valor do {x}° gasto: R$'))
        total_gasto = total_gasto + valo_gasto

    media = total_gasto / transacoes
    return transacoes, total_gasto,media


trans, total_ga, med = registros()

print(f'Você realizou {trans} transações hoje\n '
      f'Total gasto foi de R${total_ga:.2f}\n'
      f'Valor médio por transação foi de R${med:.2f}')