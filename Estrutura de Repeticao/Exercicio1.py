c = float(input('Informe o capital emprestado: '))
m = float(input('Informe a quantidade de meses para quitação: '))
if c <= 10000:
    t = 0.10
    J = c * t * m
    total = c + J
    print('Taxa de juros aplicada: 10%')
    print(f'Juros devido: {J:.2f}')
    print(f'Valor total: {total:.2f}')
else:
    t = 0.07
    J = c * t * m
    total = c + J
    print('Taxa de juros aplicada: 7%')
    print(f'Juros devido: {J:.2f}')
    print(f'Valor total: {total:.2f}')

