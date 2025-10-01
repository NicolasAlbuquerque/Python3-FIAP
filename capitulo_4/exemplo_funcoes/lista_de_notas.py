notas = []

while input('Deseja inserir uma nota? S- sim, N- não: ').upper() != 'N':
    notas.append(float(input('Por favor, insira a nota: ')))

media_aritmetica = sum(notas) / len(notas)

print(f'Para as {len(notas)} notas digitadas, a média foi de {media_aritmetica:.2f}')