from biblioteca import *
vet_prod = inputVetor('Informe os nomes dos produtos: ', str)
matriz_vend = inputMatriz('Informe as quantidades de vendas: ', int)

linhas = len(matriz_vend)
colunas = len(matriz_vend[0])

totais_vendas = []

for i in range(linhas):
    total_produto = sum(matriz_vend[i])
    totais_vendas.append(total_produto)

indice_produto_selecionado = totais_vendas.index(max(totais_vendas))
produto_selecionado = vet_prod[indice_produto_selecionado]
total_vendas_produto_selecionado = totais_vendas[indice_produto_selecionado]

print(f"Produto selecionado: {produto_selecionado}")
print(f"Total de vendas de {produto_selecionado}: {total_vendas_produto_selecionado}")