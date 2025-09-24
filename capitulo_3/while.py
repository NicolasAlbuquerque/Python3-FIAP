resposta = ''
tentativas = 0

while resposta != '42':
    resposta= input('Qual o segredo da vida, do universo e tudo mais? ')
    tentativas += 1
print('Parabéns voce acertou!\n Não esqueça sua toalha!')
print(f'Você precisou de {tentativas} tentativas')