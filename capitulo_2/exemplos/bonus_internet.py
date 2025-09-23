#Uma empresa de telefonia está realizando uma promoção, onde os clientes podem receber bônus para navegação na internet com base na sua pontuação.

# 1000 pontos: 3GB
# 500 pontos: 1,5GB
# 200 pontos: 500Mb


pontos = int(input('Informe  a quantidade de pontos: '))

if pontos >= 1000:
    print('Você recebeu 3gb de bônus.')
elif pontos >=500:
    print('Você recebeu 1,5gb de Bônus.')
elif pontos >= 200:
    print('Você recebeu 200mb de bônus  ')
else:
    print('Voê não tem pontuação suficiente para trocar por bônus de internet ')