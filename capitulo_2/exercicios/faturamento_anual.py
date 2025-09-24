
faturamento_anual = float(input('Digite o valo do seu faturamento Anual: R$ '))
assinatura = input("Digite o tipo de assinatura:\n 1 - Basic\n 2 - Silver\n 3 - Gold\n 4 - Platinum")

if assinatura == '1':
    sobre_faturamento = faturamento_anual * 0.30
    print(f'Você deve pagar {sobre_faturamento}')
elif assinatura == '2':
    sobre_faturamento = faturamento_anual * 0.20
    print(f'Você deve pagar {sobre_faturamento}')
elif assinatura == '3':
    sobre_faturamento = faturamento_anual *0.10
    print(f'Você deve pagar {sobre_faturamento}')
elif assinatura == '4':
    sobre_faturamento = faturamento_anual * 0.05
    print(f'Você deve pagar {sobre_faturamento}')
else:
    print('entrada invalida!')