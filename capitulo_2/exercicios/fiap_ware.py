valor = float(input('Digite o valor da compra: '))
cupom = input('Cupom de desconto: ')

if cupom.upper() == 'NIVER10':
    total = valor - valor * 0.1
else:
    total = valor

print(f'Valor a total a ser pago R${total:.2f}')