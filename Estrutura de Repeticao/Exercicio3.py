import math 
q = int(input('Digite a quantidade de lados: '))
if q < 3:
    print('Não é um polígono')
elif q == 3:
    L = float(input('Digite a medida do lado: '))
    A = L ** 2 * math.sqrt(3) / 4
    print(f'O polígono é um triângulo com área: {A:.2f}')
elif q == 4:
    L = float(input('Digite a medida do lado: '))
    A = L ** 2
    print(f'O polígono é um quadrado com área: {A:.2f}')
elif q == 5:
    L = float(input('Digite a medida do lado: '))
    A = 5 * L ** 2 / (4 * math.tan(0.6283))
    print(f'O polígono é um pentágono com área: {A:.2f}')
elif q == 6:
    L = float(input('Digite a medida do lado: '))
    A = 3 * L ** 2 * math.sqrt(3) / 2
    print(f'O polígono é um hexágono com área: {A:.2f}')
elif q > 6:
    print('Polígono não identificado')



    