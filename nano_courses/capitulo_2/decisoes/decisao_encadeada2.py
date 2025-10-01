nome = input("Digite o nome: ")
idade= int(input("Digite a idade: "))
infectado = input('Suspeita de doença infecto-contagiosa? ').upper()

#Primeiro problema, doença infecciosa
if infectado == 'SIM':
    print(f'Encaminha o paciente {nome} para a sala AMARELA')
elif infectado == 'NÃO':
    print(f'Encaminha o paciente {nome} para a sala BRANCA')
else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NÃO')

#Segundo problema, idade

if idade >=65:
    print('Paciente COM PRIORIDADE')
else:
    genero= input('Informe o gênero do paciente: ').upper()
    if genero == 'FEMININO' and idade >= 10:
        gravidez = input('A paciente está grávida? ').upper()
        if gravidez == 'SIM':
            print(f'Paciente COM PRIORIDADE')
        else:
            print(f'A Paciente SEM PRIORIDADE')
    else:
        print(f'O paciente {nome}, SEM PRIORIDADE')
