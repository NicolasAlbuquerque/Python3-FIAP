carrinho_de_compras= ['sabonete', 'shampoo', 'creme dental']

#INSERINDO DADOS NO FIM DA LISTA
carrinho_de_compras.append('Escova de dentes')

#INSERIR ITENS NA LISTA COM INPUT

carrinho_de_compras.append(input('Digite o item: '))

print(carrinho_de_compras)

#INSERIR DADO NUM ÍNDICE ESPECIFICO
carrinho_de_compras.insert(1,'escova de dente')
print(carrinho_de_compras)

#INSERIR DADO NUM INDICE ESPECIFICO COM INPUT
carrinho_de_compras.insert(2,'café')
carrinho_de_compras.insert(int(input('digite o local da lista: ')),input('Digite o item'))

for item in carrinho_de_compras:
    print(item)

