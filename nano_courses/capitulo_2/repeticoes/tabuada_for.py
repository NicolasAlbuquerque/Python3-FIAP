num = int(input('Digite o número para calcular a tabuada'))

for x in range(1,11,1):
    resultado = num * x
    print(f'{num} X {x} = {resultado}')