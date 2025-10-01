nome = input("Digite o nome: ")
idade= int(input("Digite a idade: "))
infectado = input('Suspeita de doença infecto-contagiosa? ').upper()
if idade >= 65 and infectado == 'SIM':
    print('O paciente ' + nome + ' será direcionado para a sala Amarela - COM PRIORIDADE ')
elif infectado == 'SIM' and idade < 65:
    print(f'O paciente {nome}, erá direcionado para a sala Amarela - SEM PRIORIDADE')
elif infectado == 'NÃO' and idade >= 65:
    print('O paciente ' + nome + ' será direcionado para a sala Branca - COM PRIORIDADE ')
elif infectado == 'NÃO' and idade < 65:
    print('O paciente ' + nome + ' será direcionado para a sala Branda - SEM PRIORIDADE ')
else:
    print('Responda a suspeita de doença contagiosa com SIM ou NÃO')