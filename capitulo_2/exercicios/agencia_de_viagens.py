# Pegar a categoria
categoria_passagem = int(input('Digite 1 -  Econômica, 2 - Executiva, 3 - Primeira classe:  '))

# Avaliar a passagem

if categoria_passagem == 1 or categoria_passagem == 2 or categoria_passagem == 3:
    ##egar os valores necessários:

    valor_bruto = float(input('Digite o valor do Pacote: R$'))
    viajantes = int(input('Quantidade de passagens: '))

    if categoria_passagem == 1:

        if viajantes == 2:
            # calculos
            desconto = valor_bruto * 0.03
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
        elif viajantes == 3:

            # calculos
            desconto = valor_bruto * 0.04
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
        elif viajantes >= 4:
            # calculos
            desconto = valor_bruto * 0.05
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
    elif categoria_passagem == 2:
        if 1 <= viajantes <= 2:
            # calculos
            desconto = valor_bruto * 0.05
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
        elif viajantes == 3:
            # calculos
            desconto = valor_bruto * 0.07
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
        else:
            # calculos
            desconto = valor_bruto * 0.08
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')

    elif categoria_passagem == 3:
        if 1 <= viajantes <= 2:
            # calculos
            desconto = valor_bruto * 0.10
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
        elif viajantes == 3:
            # calculos
            desconto = valor_bruto * 0.15
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
        else:
            # calculos
            desconto = valor_bruto * 0.20
            valor_desconto = valor_bruto - desconto
            valor_pessoa = valor_desconto / int(viajantes)
            # EXIBIR VALOR BRUTO
            print(f'Valor Bruto: R${valor_bruto:.2f}')
            # EXIBIR VALOR DO DESCONTO
            print(f'Valor do desconto: R${desconto:.2f}')
            # EXIBIR VALOR COM DESCONTO
            print(f'O valor das passagens com desconto é de: R$ {valor_desconto:.2f}')
            # EXIBIR VALOR MÉDIO POR PESSOA
            print(f'Valor por pessoa R${valor_pessoa}')
else:
    print('Categoria inválida')
