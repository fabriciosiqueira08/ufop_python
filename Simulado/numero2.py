km = float(input("Informe a distância percorrida (km): "))
percorrer = float(input("Informe a distância a percorrer (km): "))
total = km + percorrer
if total < 30:
    print('Vá a pé e busque combustivel!')
    print(f'Você percorreu {total:.0f} km')
elif total >= 30 and total < 60:
    print('Você chegará ao posto A, gasolina a R$ 4,30')
elif total >= 60 and total < 90:
    print('Você chegará ao posto B, gasolina a R$ 4,20')
elif total >= 90 and total < 120:
    print('Você chegará ao posto C, gasolina a R$ 5,10')
elif total >= 120:
    print('Você chegará ao posto D, gasolina a R$ 4,10')