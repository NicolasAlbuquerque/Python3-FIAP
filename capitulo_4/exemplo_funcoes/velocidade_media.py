
#Criando a função
def calcular_velocidade_media(distancia, tempo):

    #calcular velocidade média
    velocidade_media= distancia / tempo

    #exibir resultado
    print(f'A velocidade média é de {velocidade_media}')


# solicitar distância e tempo
distancia = float(input('Digite a Distância percorrida: '))
tempo = float(input('Digite o tempo da viagem: '))

calcular_velocidade_media(distancia,tempo) #Chamando função com valores definidos pelo usuário
calcular_velocidade_media(500,3) #chamando a função com valores definidos pelo programador

