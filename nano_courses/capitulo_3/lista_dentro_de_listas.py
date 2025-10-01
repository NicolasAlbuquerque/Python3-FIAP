inventario = [['impressora laser',850.00,123456, 'RH'],['impressora jato', 400.00 ,55478,'DP'],['servidor hp',12500.00, 12377, 'RH']]

def voltar():
    input('Aperte qualquer tecla para voltar ao menu: ')
    menu()

def exibir_produto():
    print(f'\t  \n PRODUTOS.\n')
    for linha in range(0,len(inventario)):
        print(f'\nPRODUTO {linha + 1}')
        for item in range  (0,len(inventario[linha])):
            if item == 0:
                print(f'Nome..................: {inventario[linha][item]}')
            elif item == 1:
                print(f'Valor.................: {inventario[linha][item]}')
            elif item == 2:
                print(f'Serial................: {inventario[linha][item]}')
            elif item == 3:
                print(f'Departamento..........: {inventario[linha][item]}')
            else:
                print('Inválido')
    voltar()

def buscar_produto(nome):
    for x in range(0,len(inventario)):
        if  nome == inventario[x][0]:
             print(f'Nome..................: {inventario[x][0]}')
             print(f'Valor.................: {inventario[x][1]}')
             print(f'Serial................: {inventario[x][2]}')
             print(f'Departamento..........: {inventario[x][3]}')


    voltar()






def cadastro_produto():
    resposta = 'S'
    while resposta == 'S':
        equipamento=[input('Nome do equipamento: '),float(input('Digite o valor: R$')),int(input('Número de série: ')),input('Departamento: ')]
        inventario.append(equipamento)
        resposta=input('Deseja Cadastrar mais algum produto? S - Sim | N - NÃO ')
    voltar()

def desconto(nome):
    print('\nProduto atualizado com desconto: ')
    for x in range(0,len(inventario)):
        if nome == inventario[x][0]:
            inventario[x][1] *= 0.9
            for item in range(0,len(inventario[x])):
                if item == 0:
                    print(f'Nome..................: {inventario[x][item]}')
                elif item == 1:
                    print(f'Valor.................: {inventario[x][item]}')
                    print(f'Valor com Desconto....: {inventario[x][item] * 0.9}')
                elif item == 2:
                    print(f'Serial................: {inventario[x][item]}')
                elif item == 3:
                    print(f'Departamento..........: {inventario[x][item]}')

    voltar()

def deletar_produto(nome):

    for item in range(0,len(inventario)):
        if nome == inventario[item][0]:
            del inventario[item]
            break
    exibir_produto()
    voltar()

def exibir_valores():
    valores= []
    for elementos in inventario:
        valores.append((elementos[1]))
    if len(valores) > 0:
        print(f'O equipamento mais caro custa R${max(valores)}')
        print(f'O equipamento mais barato custa R${min(valores)}')
        print(f'A total em equipamentos é de R${sum(valores)}')

    voltar()

def menu():
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
            cadastro_produto()
        case 2:
            buscar_produto(input('Digite o nome do produto: '))
        case 3:
            desconto(input('Digite o nome do produto que receberá o desconto: '))
        case 4:
            deletar_produto(input('Digite o produto que deseja excluir do sistema: '))
        case 5:
            exibir_produto()
        case 6:
            exibir_valores()
menu()

