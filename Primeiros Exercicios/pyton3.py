import math
ladrilho = int(input('Forneça o tipo de ladrilho (1 ou 2): '))
area = float(input('Forneça a área da sala: '))
lad_1 = 80
lad_2 = 60
if ladrilho == 1:
    quantidade = math.ceil(area / lad_1)
    print(f'Quantidade de ladrilhos: {quantidade}')
else:
    quantidade = math.ceil(area / lad_2)
    print(f'Quantidade de ladrilhos: {quantidade}')
