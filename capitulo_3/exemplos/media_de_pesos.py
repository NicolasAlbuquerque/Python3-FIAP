peso_total = 0.0

for c in range(1,101):
    peso_carga=float(input('Informe o peso da caixa: '))
    peso_total= peso_total + peso_carga

media= peso_total / 100

print(f'O peso total das 100 caixas é de {peso_total}kg, peso médio por caixa: {media}kg')