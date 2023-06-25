vtc = float(input('Qual o valor total da compra? '))
if vtc <= 0:
    print('Valor de compra inválido!')
if 0 < vtc <= 300:
    desconto = vtc * 0.02
    total = vtc - desconto
    print(f'Valor do pagamento: R$ {total:.2f}')
if 300 < vtc <= 600:
    desconto = vtc * 0.04
    total = vtc - desconto
    print(f'Valor do pagamento: R$ {total:.2f}')
if 600 < vtc <= 900:
    desconto = vtc * 0.06
    total = vtc - desconto
    print(f'Valor do pagamento: R$ {total:.2f}')
if vtc > 900:
    desconto = vtc * 0.08
    total = vtc - desconto
    print(f'Valor do pagamento: R$ {total:.2f}')

