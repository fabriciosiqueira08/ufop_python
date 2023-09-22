from biblioteca import *
matriz = inputMatriz('Digite os elementos da matriz:', int)

linhas = len(matriz)
colunas = len(matriz[0])

if linhas != colunas:
    print('A matriz não é quadrada')
else:
    diagonal = [matriz[i][i] for i in range (linhas)]
    print('Elementos da diagonal principal:')
    print(diagonal)