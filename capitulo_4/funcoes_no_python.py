#Trecho do código especifica que sejamos usar mais de uma vez

#CRIAÇÃO DE UMA FUNÇÃO
def calcular_velocidade_media():

    #solicitr distância e tempo
    distancia = float(input('Digite a Distância percorrida: '))
    tempo= float(input('Digite o tempo da viagem: '))

    #calcular velocidade média
    velocidade_media= distancia / tempo

    #exibir resultado
    print(f'A velocidade média é de {velocidade_media}')

calcular_velocidade_media() #chamando a função!

#PARÂMETROS

def soma(num1,num2):
    print(num1+num2)

#Chmando a função
soma(1,2)
