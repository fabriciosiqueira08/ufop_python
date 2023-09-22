vc = float(input('Valor da compra (R$): '))
n = int(input('Número de parcelas: '))

if n == 1:
    desconto = vc * 0.10
    total = vc - desconto
elif n == 2:
    total = vc
elif n == 3:
    acrescimo = vc * 0.05
    total = vc + acrescimo
elif n == 4:
    acrescimo = vc * 0.08
    total = vc + acrescimo
parcela = total / n
print(f'Valor final da compra: R$ {total:.2f}')
print(f'Parcelas: {n} x R$ {parcela:.2f}')