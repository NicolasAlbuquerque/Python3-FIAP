import math
#Solicitando os valores de A, B e C

a = float(input("Digite o valo de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#Dalculando Delta

delta = b * b + 4 * a * c

print(f'Delta = {delta}')

#Verificações das condições

if delta > 0.0:
    #calculo de dois valores para x
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'Para a equação {a}x² + {b}x + {c} = 0, obtivemos os seguintes valores: x1 = {x1} e x = {x2}')
elif delta == 0.0:
    #calculo de 1 valor para x
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f'Para a equação {a}x² + {b}x + {c} = 0, obtivemos o seguinte valor: x = {x}')
else:
    #Exibir mensagem
    print(f'Para a equação {a}x² + {b}x + {c} = 0, não existem valores reais para x.')
