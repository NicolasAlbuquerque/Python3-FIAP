
# CONECTIVO AND &&



#Para acessar um sistem, o usuário deve digitar o user name darth_vader e senha 1138
#Crie um "script" que cereba e valide estas informações de acesso


user_name = input('Digite o nome do usuário: ')
senha = input('Digite a senha: ')

if user_name.lower() == 'darth_vader' and senha == '1138':
    print('Login bem-sucedido.')
else:
    print('Login não autorizado')

