
def exibir_produto(lista):
    print(f'\t  \n PRODUTOS.\n')
    for linha in range(0,len(lista)):
        print(f'\nPRODUTO {linha + 1}')
        for item in range  (0,len(lista[linha])):
            if item == 0:
                print(f'Nome..................: {lista[linha][item]}')
            elif item == 1:
                print(f'Valor.................: {lista[linha][item]}')
            elif item == 2:
                print(f'Serial................: {lista[linha][item]}')
            elif item == 3:
                print(f'Departamento..........: {lista[linha][item]}')
            else:
                print('Inválido')


def buscar_produto(lista):
    nome= input('Digite o nome do produto: ')
    for x in range(0,len(lista)):
        if  nome == lista[x][0]:
             print(f'Nome..................: {lista[x][0]}')
             print(f'Valor.................: {lista[x][1]}')
             print(f'Serial................: {lista[x][2]}')
             print(f'Departamento..........: {lista[x][3]}')
             break
    else:
        print('Produto não encontrado')


def deletar_produto(lista):
    nome = input('Digite o produto que deseja excluir do sistema: ')
    for item in range(0,len(lista)):
        if nome == lista[item][0]:
            del lista[item]
            break
    exibir_produto(lista)






def cadastro_produto(lista):
    resposta = 'S'
    while resposta == 'S':
        equipamento=[input('Nome do equipamento: '),float(input('Digite o valor: R$')),int(input('Número de série: ')),input('Departamento: ')]
        lista.append(equipamento)
        exibir_produto(lista)
        resposta=input('Deseja Cadastrar mais algum produto? S - Sim | N - NÃO ')


def desconto(lista):
    nome =input('Digite o nome do produto que receberá o desconto: ')
    print('\nProduto atualizado com desconto: ')
    for x in range(0,len(lista)):
        if nome == lista[x][0]:
            lista[x][1] *= 0.9
            for item in range(0,len(lista[x])):
                if item == 0:
                    print(f'Nome..................: {lista[x][item]}')
                elif item == 1:
                    print(f'Valor.................: {lista[x][item]}')
                    print(f'Valor com Desconto....: {lista[x][item] * 0.9}')
                elif item == 2:
                    print(f'Serial................: {lista[x][item]}')
                elif item == 3:
                    print(f'Departamento..........: {lista[x][item]}')





def exibir_valores(lista):
    valores= []
    for elementos in lista:
        valores.append((elementos[1]))
    if len(valores) > 0:
        print(f'O equipamento mais caro custa R${max(valores)}')
        print(f'O equipamento mais barato custa R${min(valores)}')
        print(f'A total em equipamentos é de R${sum(valores)}')


