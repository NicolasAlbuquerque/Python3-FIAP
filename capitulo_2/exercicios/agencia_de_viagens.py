                #Pegar os valores necessários:

valor_bruto = float(input('Digite o valor do Pacote: R$'))
categoria_passagem = input('Digite 1 -  Econômica, 2 - Executiva, 3 - Primeira classe:  ')
viajantes = int(input('Quantidade de passagens: '))

#EXIBIR VALOR BRUTO
print(f'Valor Bruto: R${valor_bruto:.2f}')
                #Avaliar a passagem, exibir valor do desconto Exibir valor com desconto

if categoria_passagem == '1':
    if 1 <= viajantes <= 2:
        desconto = valor_bruto * 0.03
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')
    elif viajantes == 3 :
        desconto = valor_bruto * 0.04
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')

    else:
        desconto = valor_bruto * 0.05
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')

elif categoria_passagem == '2':
    if 1 <= viajantes <= 2:
        desconto = valor_bruto * 0.05
        valor_desconto = valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')
    elif viajantes == 3:
        desconto = valor_bruto * 0.07
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')
    else:
        desconto = valor_bruto * 0.08
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')

elif categoria_passagem == '3':
    if 1 <= viajantes <=2:
        desconto = valor_bruto * 0.10
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa =  valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')
    elif viajantes == 3:
        desconto = valor_bruto * 0.15
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')
    else:
        desconto = valor_bruto * 0.20
        valor_desconto= valor_bruto - desconto
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
        valor_pessoa = valor_desconto / int(viajantes)
        print(f'Valor por pessoa R${valor_pessoa}')
