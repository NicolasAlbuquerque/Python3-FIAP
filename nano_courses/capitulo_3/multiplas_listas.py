
lista_equip = ['impressora 1', 'impressora 2',  'monitor', 'mouse', 'teclado','placa de rede']
lista_valor = [400.50, 500, 1200, 70, 120, 400]
lista_numero_serial = [12,34,56,78,91,32]
lista_departamento = ['impressoras','impressoras', 'perifericos','perifericos','perifericos','perifericos']

def voltar():
    input('Aperte qualquer tecla para voltar ao menu: ')
    menu()

def cadastrar_produto():
    resposta = 'S'


    while resposta == 'S':
        lista_equip.append(input('Digite o nome do equipamento: '))
        lista_valor.append(float(input('Digite o valor: ')))
        lista_numero_serial.append(int(input('Digite o número de série: ')))
        lista_departamento.append(input('Departamento: '))
        resposta=input('Deseja continuar S ou N? ').upper()
        voltar()


def listar():
    for x in range(0,len(lista_equip)):
        print(f'\n \tPRODUTO....{x+1}')
        print(f'Nome...............: {lista_equip[x]}')
        print(f'Valor..............: {lista_valor[x]}')
        print(f'Serial.............: {lista_numero_serial[x]}')
        print(f'Departamento.......: {lista_departamento[x]}')
    voltar()

def buscar_produto(buscar):

    for indice in range(0,len(lista_equip)):
            if buscar == lista_equip[indice]:
                print(f'Nome.......: {lista_equip[indice]}')
                print(f'Valor......: {lista_valor[indice]}')
                print(f'Serial.....: {lista_numero_serial[indice]}')
    voltar()


def desconto(desc):

    for x in range(0,len(lista_equip)):
        if lista_equip[x]== desc:
            print(f'\nNome.......: {lista_equip[x]}')
            print(f'Valor......: {lista_valor[x]}')
            print(f'Serial.....: {lista_numero_serial[x]}')
            print(f'Valor Desconto.....: {lista_valor[x] * 0.9}')
            print(f'Departamento.......: {lista_departamento[x]}')
    voltar()


def deletar_produto(deletar):
    print(f'\nDELETANDO ITEM: {deletar.upper()}')
    for x in range(0,len(lista_equip)):
        if deletar == lista_equip[x]:
            del lista_departamento[x]
            del lista_equip[x]
            del lista_valor[x]
            del lista_numero_serial[x]
            break

    listar()


def menu():
    opcao= 0
    while opcao != 1 and opcao != 2 and opcao !=3 and opcao != 4 and opcao != 5:
        print(' --------------------Menu-------------------------')
        print('|1- Cadastro de produto     2 - Pesquisar produto |')
        print('|3- Aplicar desconto        4- Deletar produto    |')
        print('|5- Listar produtos                               |')
        print(' -------------------------------------------------')
        opcao = int(input('Digite a opção desejada 1, 2, 3, 4, 5'))
    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            buscar_produto(input('Digite o equipamento que deseja: '))
        case 3:
            desconto(input('Digite o nome do equipamento a receber o desconto: ')
)
        case 4:
            deletar_produto(input('Informe o item danificado: '))
        case 5:
            listar()
menu()