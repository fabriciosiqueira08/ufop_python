from biblioteca import *

matriz1 = inputMatriz('Imagem 1: ', int)
matriz2 = inputMatriz('Imagem 2: ', int)

linhas = len(matriz1)
colunas = len(matriz1[0])

similiaridade = 0
for i in range (linhas):
    for j in range (colunas):
        if matriz1[i][j] == matriz2[i][j]:
            similiaridade += 1
porcentagem = (similiaridade / (linhas * colunas)) * 100
if porcentagem == 100:
    print('As imagens são iguais!')
else:
    print('As imagens são diferentes!')
    print(f'Porcentagem de similiaridade: {porcentagem:.2f}%')
