import math
lad = int(input('Forneça o tipo de ladrilho(1/2/3)? '))
if lad == 1:
    lad1 = 80
    sala = float(input('Qual a área da sala? '))
    quant = math.ceil(sala / lad1)
    print(f'Quantidade de ladrilhos: {quant:.0f}')
if lad == 2:
    lad2 = 60
    sala = float(input('Qual a área da sala? '))
    quant = math.ceil(sala / lad2)
    print(f'Quantidade de ladrilhos: {quant:.0f}')
if lad == 3:
    lad3 = 40
    sala = float(input('Qual a área da sala? '))
    quant = math.ceil(sala / lad3)
    print(f'Quantidade de ladrilhos: {quant:.0f}')
if lad > 3:
    print(f'ERRO: o ladrilho tipo {lad} é invalido.')