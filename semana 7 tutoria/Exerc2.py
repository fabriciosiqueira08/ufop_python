def Calculos(sm,qr):
    valorqr = sm / 7 / 100
    vp = valorqr * qr
    desconto = vp * 0.10
    novovalor = vp - desconto
    return valorqr, vp, novovalor

print('Cálculo do Custo de Energia')
salariom = float(input('Salário mínimo: '))
quantidadew = float(input('Quantidade de quilowatts: '))
valorqr, vp, novovalor = Calculos(salariom, quantidadew)
print(f'Valor de cada quilowatt: R$ {valorqr:.2f}')
print(f'Valor a ser pago: R$ {vp:.2f}')
print(f'Valor a ser pago com desconto de 10%: R$ {novovalor:.2f}')


