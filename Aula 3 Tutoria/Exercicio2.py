print('CÁLCULO DO IMPOSTO - DÓLAR AUSTRALIANO (AUD$)')
renda = float(input('DIGITE A RENDA TRIBUTÁVEL DO CIDADÃO: '))

if 0 < renda <= 6000:
    print(f'RENDA TRIBUTAVEL: AU$ {renda:.2f}')
    imposto = 0.00
    saude = renda * 1.5 / 100
    total = imposto + saude
    print(f'IMPOSTO DEVIDO: AU$ {imposto:.2f}')
    print(f'IMPOSTO PARA SAÚDE - Druken Clam: AU$ {saude:.2f}')
    print(f'IMPOSTO TOTAL A SER PAGO: AU$ {total:.2f}')
elif 6001 <= renda <= 20000:
    print(f'RENDA TRIBUTAVEL: AU$ {renda:.2f}')
    imposto = 0.17 * (renda - 6000) 
    saude = renda * 1.5 / 100
    total = imposto + saude
    print(f'IMPOSTO DEVIDO: AU$ {imposto:.2f}')
    print(f'IMPOSTO PARA SAÚDE - Druken Clam: AU$ {saude:.2f}')
    print(f'IMPOSTO TOTAL A SER PAGO: AU$ {total:.2f}')
elif 20001 <= renda <= 40000:
    print(f'RENDA TRIBUTAVEL: AU$ {renda:.2f}')
    imposto = 2380 + 0.30 * (renda - 20000)
    saude = renda * 1.5 / 100
    total = imposto + saude
    print(f'IMPOSTO DEVIDO: AU$ {imposto:.2f}')
    print(f'IMPOSTO PARA SAÚDE - Druken Clam: AU$ {saude:.2f}')
    print(f'IMPOSTO TOTAL A SER PAGO: AU$ {total:.2f}')
elif 50001 <= renda <= 60000:
    print(f'RENDA TRIBUTAVEL: AU$ {renda:.2f}')
    imposto = 11380 + 0.42 * (renda - 50000)
    saude = renda * 1.5 / 100
    total = imposto + saude
    print(f'IMPOSTO DEVIDO: AU$ {imposto:.2f}')
    print(f'IMPOSTO PARA SAÚDE - Druken Clam: AU$ {saude:.2f}')
    print(f'IMPOSTO TOTAL A SER PAGO: AU$ {total:.2f}')
else:
    print(f'RENDA TRIBUTAVEL: AU$ {renda:.2f}')
    imposto = 15580 + 0.47 * (renda - 60000)
    saude = renda * 1.5 / 100
    total = imposto + saude
    print(f'IMPOSTO DEVIDO: AU$ {imposto:.2f}')
    print(f'IMPOSTO PARA SAÚDE - Druken Clam: AU$ {saude:.2f}')
    print(f'IMPOSTO TOTAL A SER PAGO: AU$ {total:.2f}')

