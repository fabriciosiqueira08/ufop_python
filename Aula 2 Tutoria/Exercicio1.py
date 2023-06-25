vc = float(input('Informe o valor da compra: R$'))
if vc <= 150:
    desconto = vc * 0.10
    cd = vc - desconto
    imposto = cd * 0.08
    total = cd + imposto
    print(f'Valor do desconto: R$ {desconto:.2f}')
    print(f'Valor da compra com desconto: R$ {cd:.2f}')
    print(f'Valor do imposto: R$ {imposto:.2f}')
    print(f'Valor total da compra: R$ {total:.2f}')
else:
    desconto = vc * 0.20
    cd = vc - desconto
    imposto = cd * 0.08
    total = cd + imposto
    print(f'Valor do desconto: {desconto:.2f}')
    print(f'Valor da compra com desconto: {cd:.2f}')
    print(f'Valor do imposto: {imposto:.2f}')
    print(f'Valor total da compra: {total:.2f}')

