

#Duranteo aniversário da sua fundação, uma loja está presenteando clientes da seguinte forma:
#Todas as compras de calor superior a R$ 1000,00, receberão um desconto de 10%
#Clientes selecionados receberão o cumpom FESTA, que também gera 10% de desconto na hora da compra, não importa o valor
# descontos não são cumulativos
#Escreva um script que receba um cumpom e o valor de uma compra do usuário e informe o valor da compra

valor = float(input('Informe o valor da compra: '))
cupom = input('Cumpom de desconto: ')
total= 0

if valor >= 1000 or cupom.lower() == 'festa':
    total = valor * 0.9
    print(f'Total a pagar com desconto {total} ')
else:
    total = valor

print(f'Valor total a pagar {total}')