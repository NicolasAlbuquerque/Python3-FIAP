resposta = input('Deseja cadastrar outro paciente? SIM ou NÃO').upper()
while resposta != 'SIM' and resposta != 'NÃO':
    print('Responda SIM ou NÃO. ')
    resposta = input('Deseja cadastrar outro paciente? SIM ou NÃO').upper()

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
infectado = input('Suspeita de doença infecto-contagiosa? ').upper()

while infectado != 'SIM' and infectado != 'NÃO':
    print('Digite SIM ou NÃO..')
    infectado = input('Suspeita de doença infecto-contagiosa? ').upper()

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
print('Finalizando app')