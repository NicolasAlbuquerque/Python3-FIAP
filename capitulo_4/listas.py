#CRIAR LISTA VAZIA
jedi = []

print(type(jedi))
#CRIAÇÃO DE UMA LISTA COM OS JEDI
jedi= ['Luke', 'Yoda','Obi-Wan', 'Anakin']

#EXIBIÇÃO DE UMA LISTA COMPLETA
print('versão um ', jedi)

#EXIBIÇÃO DE UMA POSIÇÃO ESPECIFICA NA LISTA
print(jedi[0])

#EXIBIÇÃO DO ÚLTIMO ELEMENTO
print(jedi[-1])

#EXIBIR um SUBESPAÇO - INTERVALO
print(jedi[0:3]) #entre o 1 e o 3

#exibição de cada item da lista
for nome in jedi:
    print(nome)


#INSERIR DADOS NO FIM DA LISTA
jedi.append('Luminara')
print(f'Apos a inserção a lista contem: \n {jedi}')

#INSERIR DADOS COM INPUT
jedi.append(input('Digite o nome do Jedi: '))

#INSERIR VALOR EM UAM POSIÇÃO ESPECIFICA
jedi.insert(0, 'Mace Windu')
print(jedi)

print(jedi)


#REMOVER O ULTIMO ELEMENTO
jedi.pop()
print(jedi)

#REMOVER VALOR EM POSIÇÃO ESPECÍFICA
jedi.pop(1)
print(jedi)

#REMOÇÃO DE UM ITEM ESPECÍFICO
jedi.remove('Obi-Wan')
print(jedi)

#APAGAR LISTA TODA
jedi.clear()
print(jedi)


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
print(f'A quantidade de elementos na lista é de: {quantidade} itens')

#SOMAR TODOS OS ELEMENTOS
soma= sum(valores)
print(f'A soma dos valores é de: {soma}')