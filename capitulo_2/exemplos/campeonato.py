age= int(input('Informe sua idade'))
rm = input('Informe o seu RM: ')

if age >= 18:
    print(f'aluno do nm: {rm}, foi registrado')
    print('Mais informações serão enviadas para o seu e-mail cadastrado.')
else:
    autorization = input('Tem Autorização dos pais? S - Sim,  N - Não.')
    if autorization == 'S':                                                      # Desvios encadeados são aqueles que colocamos um desvio dentro do outro
        print(f'A participação do aluno do RM {rm}, foi autorizada.')
        print('Mais informações serão encaminhadas para o e-mail cadastrado.')
    else:
        print('Participação não autorizado por conta da idade.')