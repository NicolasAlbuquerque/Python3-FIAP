nivel_de_acesso = input('Informe o nível de acesso (ADM, USR, GUEST)').upper()
genero = input('Informe o gênero: ').upper()
categoria= ''
if genero == 'FEMININO':
    if nivel_de_acesso == 'ADM':
        categoria = 'administradora'
    elif nivel_de_acesso == 'USR':
        categoria= 'usuária'
    elif nivel_de_acesso == 'GUEST':
        categoria= 'visitante'
    else:
        print('Informe o gênero.')
    print(f'Olá {categoria}')
elif genero == 'MASCULINO':
    if nivel_de_acesso == 'ADM':
        categoria = 'administrador'
    elif nivel_de_acesso == 'USR':
        categoria = 'usuário'
    elif nivel_de_acesso == 'GUEST':
        categoria = 'visitante'
    else:
        print('Informe o gênero.')
    print(f'Olá {categoria}')
else:
    print('Olá desconhecido')