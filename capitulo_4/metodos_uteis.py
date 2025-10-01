#Valores fora da order

valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]

#Exibição da lista
print('A lista foi criada assim: {}'.format(valores))

#contagem de elementos
contagem = valores.count(7)
print(f'contagem foi de {contagem}')

#IVERTER A ORDEM DOS ELEMENTOS
valores.reverse()
print(f'A lista invertida é assim {valores}')

#ORDENAR A LISTA
#ordem crescente
valores.sort()
print(f'Ordenar em ordem crescente {valores}')
#Ordem decrescente
valores.sort(reverse=True)
print(valores)

#QUANTIDADE DE ELEMENTOS
quantidade= len(valores)
print(f'A quantidade de elementoss na lista é de: {quantidade} itens')

#SOMAR TODOS OS ELEMENTOS
soma= sum(valores)
print(f'A soma dos valores é de: {soma}')