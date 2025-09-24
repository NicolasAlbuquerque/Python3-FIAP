num = int(input('Digite um numero inteiro: '))

#if num = 1:
 #   num == num-1 + num
anterior1= 1
anterior2= 0

for x in range(1,num+1):
    atual= anterior1+anterior2
    anterior1= anterior2
    anterior2= atual

    if num == atual:
        print('Ação bem sucedida')
        break
    elif num < atual:
        print('Ação falhou')
        break
