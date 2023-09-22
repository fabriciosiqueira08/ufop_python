from biblioteca import *

def somaMatriz(matriz1, matriz2):
    matriz3 = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j] + matriz2[i][j])
        matriz3.append(linha)
    return matriz3

matriz1 = inputMatriz('Digite a primeira matriz: ', int)
matriz2 = inputMatriz('Digite a segunda matriz: ', int)

linhas = len(matriz1)
colunas = len(matriz1[0])

linhas2 = len(matriz2)
colunas2 = len(matriz2[0])

if linhas != linhas2 or colunas != colunas2:
    print('Não é possível somar as matrizes')
else:
    matriz3 = somaMatriz(matriz1, matriz2)
    print('Matriz resultante:')
    for linha in matriz3:
        print(linha)
