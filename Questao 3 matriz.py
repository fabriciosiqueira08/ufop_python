from biblioteca import *
matriz = inputMatriz('Digite os elementos da matriz: ', int)

linhas = len(matriz)
colunas = len(matriz[0])

identidade = True

for i in range(linhas):
    for j in range(colunas):
        if i == j and matriz[i][j] != 1:
            identidade = False
            break
        elif i != j and matriz[i][j] != 0:
            identidade = False
            break

if identidade:
    print('A matriz é identidade.')
else:
    print('A matriz não é identidade.')