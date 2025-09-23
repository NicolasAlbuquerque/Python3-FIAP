playstion =0
xbox = 0
nintendo = 0

print('Escolha qual console deseja ganhar: ')
voto1= input('Digite 1 - Playstation, 2 - XBOX, 3 - NINTENDO. ')
if voto1 == '1':
    playstion += 1
elif voto1 == '2':
    xbox += 1
elif voto1 == '3':
    nintendo += 1
else :
    print('Voto inválido')

print(f'SCORE: Playstation {playstion}, XBOX {xbox}, NINTENDO {nintendo}')


print('Escolha qual console deseja ganhar: ')
voto2= input('Digite 1 - Playstation, 2 - XBOX, 3 - NINTENDO. ')
if voto2 == '1':
    playstion += 1
elif voto2 == '2':
    xbox += 1
elif voto2 == '3':
    nintendo += 1
else :
    print('Voto inválido')
print(f'SCORE: Playstation {playstion}, XBOX {xbox}, NINTENDO {nintendo}')

print('Escolha qual console deseja ganhar: ')
voto3= input('Digite 1 - Playstation, 2 - XBOX, 3 - NINTENDO. ')
if voto3 == '1':
    playstion += 1
elif voto3 == '2':
    xbox += 1
elif voto3 == '3':
    nintendo += 1
else :
    print('Voto inválido')
print(f'SCORE: Playstation {playstion}, XBOX {xbox}, NINTENDO {nintendo}')


print('Escolha qual console deseja ganhar: ')
voto4= input('Digite 1 - Playstation, 2 - XBOX, 3 - NINTENDO. ')
if voto4 == '1':
    playstion += 1
elif voto4 == '2':
    xbox += 1
elif voto4 == '3':
    nintendo += 1
else :
    print('Voto inválido')
print(f'SCORE: Playstation {playstion}, XBOX {xbox}, NINTENDO {nintendo}')


print('Escolha qual console deseja ganhar: ')
voto5= input('Digite 1 - Playstation, 2 - XBOX, 3 - NINTENDO. ')
if voto5 == '1':
    playstion += 1
elif voto5 == '2':
    xbox += 1
elif voto5 == '3':
    nintendo += 1
else :
    print('Voto inválido')
print(f'SCORE: Playstation {playstion}, XBOX {xbox}, NINTENDO {nintendo}')

#COMPARANDO MAIOR
if playstion > xbox and playstion > nintendo:
    console = 'Playstation'
    print(f"E o console escolhido foi o : {console}")
elif xbox > playstion and xbox > nintendo:
    console =  'Xbox'
    print(f"E o console escolhido foi o : {console}")
elif nintendo > xbox and nintendo > playstion:
    console = 'Nintendo'
    print(f"E o console escolhido foi o : {console}\n")
else:
    print('Deu empate, votem novamente.')



