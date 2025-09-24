quantidade_de_alimentos = int(input('Informe a quantidade de alimentos ingeridos hoje: '))
calorias = 0
for x in range(1, quantidade_de_alimentos+1):
    calorias = calorias + int(input(f'Calorias do {x}° alimento: '))

print(f'O total de calorias egeridas: {calorias}')