
#Criando a função
def calcular_velocidade_media(distancia, tempo):

    #calcular velocidade média
    velocidade_media= distancia / tempo

    #retornar valor
    return velocidade_media

velocidades_medias= []
for dia in ['segunda','terça','quarta', 'quinta','sexta']:
    dist=float(input(f'Digite a velocidade distância percorrida na {dia}: '))
    temp= float(input(f'Digite o tempo da viagem na {dia}: '))
    velocidades_medias.append(calcular_velocidade_media(dist,temp))
print(f'As velocidades médias da semana foram: {velocidades_medias}')
