idade = int(input("Informe sua idade: "))
bpm = int(input('Informe os batimentos por minuto: '))

if 1<= idade <= 5:
    if 80 <= bpm <= 120:
        print('Batimentos dentro da faixa adequada.')
    elif bpm < 80:
        print('Batimentos abaixo da faixa adequada.')
    elif bpm > 120:
        print('Batimentos acima da faixa adequada.')


elif 6 <= idade <= 12:
    if 70 <= bpm <= 120:
        print('Batimentos dentro da faixa adequada.')
    elif bpm < 70:
        print('Batimentos abaixo da faixa adequada.')
    else:
        print('Batimentos acima da faixa adequada.')

elif 13 <= idade <= 18:
    if 60 <= bpm <= 100:
        print('Batimentos dentro da faixa adequada.')
    elif bpm < 60:
        print('Batimentos abaixo da faixa adequada.')
    else:
        print('Batimentos acima da faixa adequada.')

elif 19 <= idade <= 60:
    if 60 <= bpm <= 100:
        print('Batimentos dentro da faixa adequada.')
    elif bpm < 60:
        print('Batimentos abaixo da faixa adequada.')
    else:
        print('Batimentos acima da faixa adequada.')

else:
    if 60 <= bpm <= 90:
        print('Batimentos dentro da faixa adequada.')
    elif bpm < 60:
        print('Batimentos abaixo da faixa adequada.')
    else:
        print('Batimentos acima da faixa adequada.')



