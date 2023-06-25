juiz = str(input('Informe o nome do juiz: '))
qtd = int(input('Informe a quantidade de partidas: '))
totalimp = 0
totalfalt = 0
totalcart = 0
totalt = 0
for i in range (0,qtd):
    print('')
    print(f'Partida {i+1}:')
    imp = int(input('. Informe impedimentos.......: '))
    falt = int(input('. Informe faltas.............: '))
    cart = int(input('. Informe cartões............: '))
    t = float(input('. Informe tempo de acréscimo.: '))
    totalimp = totalimp + imp
    totalfalt = totalfalt + falt
    totalcart = totalcart + cart
    totalt = totalt + t
    i += 1
medimp = totalimp/qtd
medfalt = totalfalt/qtd
medcart = totalcart/qtd
medt = totalt/qtd
print('')
print(f'Estatísticas do juiz {juiz}:')
print(f'. Impedimentos.......: {medimp:.2f}.')
print(f'. Faltas.............: {medfalt:.2f}.')
print(f'. Cartões............: {medcart:.2f}.')
print(f'. Tempo de acréscimo.: {medt:.2f}.')








