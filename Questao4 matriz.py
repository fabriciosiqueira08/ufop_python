from biblioteca import *

notas = inputMatriz('Digite a matriz de notas: ', float)

linhas = len(notas)
colunas = len(notas[0])

menor_nota = float('inf')
indices_menor_nota = []

maior_nota = float('-inf')
indices_maior_nota = []

for i in range(linhas):
    for j in range(colunas):
        nota = notas[i][j]
        if nota < menor_nota:
            menor_nota = nota
            indices_menor_nota = [i]
        elif nota == menor_nota:
            indices_menor_nota.append(i)
        
        if nota > maior_nota:
            maior_nota = nota
            indices_maior_nota = [i]
        elif nota == maior_nota:
            indices_maior_nota.append(i)

print(f'Menor nota: {menor_nota:.1f}')
print('Alunos com a menor nota:')
for indice in indices_menor_nota:
    print(f'. {indice}')

print(f'\nMaior nota: {maior_nota:.1f}')
print('Alunos com a maior nota:')
for indice in indices_maior_nota:
    print(f'. {indice}')
