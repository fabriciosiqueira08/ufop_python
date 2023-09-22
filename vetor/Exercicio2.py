from biblioteca import * 

def estatNotas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    return maior, menor, media

def acimaMedia(notas, media):
    acima_indices = []
    acima_valores = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima_indices.append(i)
            acima_valores.append(notas[i])
    return acima_indices, acima_valores

def exameEspecial(notas):
    indice_exame = []
    valores_exame = []
    for i in range(len(notas)):
        if notas[i] >= 3 and notas[i] < 6:
            indice_exame.append(i)
            valores_exame.append(notas[i])
    return indice_exame, valores_exame


notas = inputVetor('Digite as notas: ', float)
alunos = inputVetor('Digite os nomes: ', str)

maior, menor, media = estatNotas(notas)
indices_acima, valores_acima = acimaMedia(notas, media)
indices_exame, valores_exame = exameEspecial(notas)

print(f'Maior nota: {maior:.1f}')
print(f'Menor nota: {menor:.1f}')
print(f'Nota média: {media:.1f}')
print('Notas acima da média: ')
for i in range(len(indices_acima)):
    print(f'  - [{indices_acima[i]:.0f}] = {valores_acima[i]:.1f} ({alunos[indices_acima[i]]})')
print('Notas em Exame Especial:')
for i in range(len(indices_exame)):
    print(f'  - [{indices_exame[i]:.0f}] = {valores_exame[i]:.1f} ({alunos[indices_exame[i]]})')