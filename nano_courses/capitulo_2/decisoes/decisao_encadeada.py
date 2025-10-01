nome = input("Digite o nome: ")
idade= int(input("Digite a idade: "))
infectado = input('Suspeita de doença infecto-contagiosa? ').upper()
if idade >= 65:
    print('O paciente ' + nome + 'COM PRIORIDADE')
    if infectado == 'SIM':
        print('Encaminhe o paciente para a sala AMARELA')
    elif infectado == 'NÃO':
        print('Encaminhe o paciente para a sala BRANCA')
    else:
        print('Responda a suspeita de doença contagiosa com SIM ou NÃO')
else:
    print(f'O paciente {nome}, SEM PRIORIDADE')
    if infectado == 'SIM':
        print('Encaminhe o paciente para a sala AMARELA')
    elif infectado == 'NÃO':
        print('Encaminhe o paciente para a sala BRANCA')
    else:
        print('Responda a suspeita de doença contagiosa com SIM ou NÃO')