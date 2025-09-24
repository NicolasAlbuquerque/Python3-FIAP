#LIBERDADE + fatorial do numero de minutos
from traceback import print_tb

senha ='LIBERDADE'
minutos = int(input('Digite os minutos do relógio: '))
fatorial = minutos
senha= senha + str(fatorial)

for x in range(1,minutos):
    fatorial= fatorial * x


print(f'A senaha é {senha}{fatorial}')