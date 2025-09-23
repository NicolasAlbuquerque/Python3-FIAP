# IF SIMPLES

#Uma universidade realizará uma competição acadêmica. Para esta competição só serão aceitos estudantes que sejam maiores
#crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso estudante seja maior


rm= input('Informe o seu RM: ')# A FUNÇÂO INPUT TRATA TUDO COMO TEXTO
idade = int(input('Digite sua idade: ')) #ESPECIFICAR O TIPO DE DADO A SER TRABALHADO


#           IF SIMPLES

if idade >= 18 :                                                      #teste
    print(f'O aluno do RM:{rm}, foi registrado com sucesso.')         #execulta caso seja verdadeiro155
    print('Os detalhes serão enviado para o seu email')




#--------------------------------------------------------------------------------------------------------------------
    
#           IF COMPOSTO

iid= input("informe o numero da matricula: ")
age= int(input('Informe sua idade: '))

if age >= 18:
    print(f'aluno do nm: {iid}, foi registrado')
    print('Mais informações serão enviadas para o seu e-mail cadastrado.')
else:

    print('Sua participação não foi autorizada por conta da sua idade.')  #a ação só é executada caso o primeiro desvio não seja executado

#---------------------------------------------------------------------------------------------------------------------

#          IF ENCADEADO


if age >= 18:
    print(f'aluno do nm: {iid}, foi registrado')
    print('Mais informações serão enviadas para o seu e-mail cadastrado.')
else:
    autorization = input('Tem Autorização dos pais? S - Sim,  N - Não.')
    if autorization == 'S':                                                      # Desvios encadeados são aqueles que colocamos um desvio dentro do outro
        print(f'A participação do aluno do RM {iid}, foi autorizada.')
        print('Mais informações serão encaminhadas para o e-mail cadastrado.')
    else:
        print('Participação não autorizado por conta da idade.')



#-----------------------------------------------------------------------------------------------------------------------

#               ELIF


pontos = int(input('Informe  a quantidade de pontos: '))

if pontos >= 1000:
    print('Você recebeu 3gb de bônus.')
elif pontos >=500:
    print('Você recebeu 1,5gb de Bônus.')
elif pontos >= 200:
    print('Você recebeu 200mb de bônus  ')
else:
    print('Voê não tem pontuação suficiente para trocar por bônus de internet ')
