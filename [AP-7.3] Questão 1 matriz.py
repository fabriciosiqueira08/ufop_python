from biblioteca import *

aux = inputMatriz('Digite os elementos da matriz: ', float)
print('')
coluna = int(input('Digite a coluna que será alterada: '))
while coluna < 0 or coluna > len(aux[0]) - 1:
    coluna = int(input('Digite uma coluna válida: '))

for i in range(len(aux)):
    aux[i][coluna] = aux[i][coluna] * 2

print('')
print('Matriz Alterada:')
for row in aux:
    formatted_row = " ".join("{:.0f}".format(value) for value in row)
    print(formatted_row)
