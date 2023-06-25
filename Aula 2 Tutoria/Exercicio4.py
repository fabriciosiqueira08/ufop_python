energia = float(input('Digite o consumo de energia elétrica (kw): '))
taxa = 5.00
print(f'Taxa básica: R$ {taxa:.2f}')
print(f'Consumo (k): {energia:.0f} ')
if energia <= 0:
    print('ERRO: o consumo deve ser inteiro e positivo (não nulo).')
if 0 < energia <= 500:
    consumo = energia * 0.02
    total = consumo + taxa 
    print(f'Valor da conta: R$ {total:.2f}')
if 500 < energia <= 1000:
    consumo = 10 + (energia - 500 ) * 0.05
    total = consumo + taxa
    print(f'Valor da conta: R$ {total:.2f}')
if energia > 1000:
    consumo = 35 + (energia - 1000) * 0.10
    total = consumo + taxa
    print
    print(f'Valor da conta: R$ {total:.2f}')
print('Fim do programa')

