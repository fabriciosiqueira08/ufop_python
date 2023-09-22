from biblioteca import *

atleta1 = inputMatriz('Informe os resultados do atleta 1: ', int)
atleta2 = inputMatriz('Informe os resultados do atleta 2: ', int)

linhas1 = len(atleta1)
colunas1 = len(atleta1[0])

linhas2 = len(atleta2)
colunas2 = len(atleta2[0])

if linhas1 != linhas2 or colunas1 != colunas2:
    print('Matrizes incompatíveis.')
else:
    vitorias_atleta1 = 0
    vitorias_atleta2 = 0
    empates = 0

    for i in range(linhas1):
        for j in range(colunas1):
            if atleta1[i][j] > atleta2[i][j]:
                vitorias_atleta1 += 1
            elif atleta1[i][j] < atleta2[i][j]:
                vitorias_atleta2 += 1
            else:
                empates += 1
              
    print(f"Quantidade de vitórias do atleta 1: {vitorias_atleta1}")
    print(f"Quantidade de vitórias do atleta 2: {vitorias_atleta2}")
    print(f"Quantidade de empates: {empates}")