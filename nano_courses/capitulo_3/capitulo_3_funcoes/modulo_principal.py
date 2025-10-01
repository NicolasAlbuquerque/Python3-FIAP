from nano_courses.capitulo_3.capitulo_3_funcoes.identificacao_de_funcoes import *

minha_lista = [['impressora laser',850.00,123456, 'RH'],['impressora jato', 400.00 ,55478,'DP'],['servidor hp',12500.00, 12377, 'RH']]


opcao= 0
while opcao != 1 and opcao != 2 and opcao !=3 and opcao != 4 and opcao != 5 and opcao != 6:
    print(' --------------------Menu-------------------------')
    print('|1- Cadastro de produto   2 - Pesquisar produto   |')
    print('|3- Aplicar desconto      4- Deletar produto      |')
    print('|5- Listar produtos       6- Valor em mercadoria  |')
    print(' -------------------------------------------------')
    opcao = int(input('Digite a opção desejada 1, 2, 3, 4, 5 ' ))
match opcao:
    case 1:
        cadastro_produto(minha_lista)
    case 2:
        buscar_produto(minha_lista)
    case 3:
        desconto(minha_lista)
    case 4:
        deletar_produto(minha_lista)
    case 5:
            exibir_produto(minha_lista)
    case 6:
            exibir_valores(minha_lista)
