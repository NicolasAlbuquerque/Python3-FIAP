
numero_combo = int(input('Digite o numero do combo desejado: '))

match numero_combo:
    case 1 :
        nome_prato = 'Hamburguer'
        valor_prato = 12.50
    case 2 :
        nome_prato = 'Cheeseburguer'
        valor_prato = 15.00
    case 3 :
        nome_prato = 'X-Baccon'
        valor_prato = 17.50
    case _:
        nome_prato= None
        valor_prato= None

if nome_prato:
    print(f'O combo desejado foi {nome_prato} e custa R${valor_prato}')