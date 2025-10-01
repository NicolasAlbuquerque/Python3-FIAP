nivel=input('Digite o nível de acesso: (ADM, USR, GUEST)').upper()
if nivel== 'ADM' or 'USR':
    genero= input('Digite o seu gênero: ').upper()
    if nivel == 'ADM':
        if genero == 'FEMININO':
            print('Olá Administradora.')
        else:
            print('Olá Administrador.')
    else:
        if genero == 'FEMININO':
            print('Olá usuária')
        else:
            print('Olá usuário')
elif nivel == 'GUEST':
    print('Olá visitante!')
else:
    print('Olá desconhecido"')