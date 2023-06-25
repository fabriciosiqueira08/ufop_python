M14 = float(input('Informe a média móvel dos últimos 14 dias: '))
A6 = float(input('Informe o somatório dos casos dos últimos 6 dias: '))
H = float(input('Informe a quantidade de casos de hoje: '))
M7 = (A6 + H) / 7
d = M14 - M7
tx = d / M14 * 100
if tx <= 0:
    print(f'Casos diminuindo em {tx:.2f}%')
elif tx <= 15:
    print(f'Casos estáveis em {tx:.2f}%')
else:
    print(f'Casos aumentando em {tx:.2f}%')