from biblioteca import *

cand = inputVetor('Digite os nomes dos candidatos: ', str)
votos = inputVetor('Digite as quantidades de votos: ', int)


if len(cand) != len(votos) or len(votos) != len(cand):
    print('Vetores com tamanhos diferentes')
elif len(cand) < 3:
    print('Quantidade de candidatos insuficiente')


maior= 0
for i in range(len(votos)):
    if votos[i] > votos[maior]:
        maior = i


print(f'Vencedor das eleições: {cand[maior]}' )