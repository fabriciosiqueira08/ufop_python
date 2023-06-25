r = float(input('Digite o valor do raio: '))
h = float(input('Digite o valor da altura: '))
c = float(input('Digite a capacidade (m3) de armazenamento do comb. dos caminhões:'))
v = 3.14159*(r**2)*h
n = v/c
print(f'O volume do reservatório é {v:.2f} m3.')
print(f'{n:.0f} caminhões poderiam ser abastecidos com este reservatório.')