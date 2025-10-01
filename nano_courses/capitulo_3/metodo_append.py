inventario = []
resposta ='S'
while resposta == 'S':
    inventario.append(input('Equipamento: '))
    inventario.append((float(input('Valor: '))))
    inventario.append(int(input('Numero serial: ')))
    inventario.append(input('Departamento: '))
    resposta= input('Deseja continuar? S- Sim N- Não').upper()

for elemento in inventario:
    print(elemento)