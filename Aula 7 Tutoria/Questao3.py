p = int(input('Digite a quantidade de pacientes: '))
somama = 0
somaob = 0
for i in range(0,p):
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = peso/(altura**2)
    if imc < 16:
        print(f'O IMC é {imc:.2f} ==> Magreza extrema')
        somama += 1
    elif 16 <= imc < 18.5:
        print(f'O IMC é {imc:.2f} ==> Abaixo do peso')
    elif 18.5 <= imc < 25:
        print(f'O IMC é {imc:.2f} ==> Saudavel')
    elif 25 <= imc < 30:
        print(f'O IMC é {imc:.2f} ==> Sobrepeso')
    elif 30 <= imc < 40:
        print(f'O IMC é {imc:.2f} ==> Obesidade')
    else:
        print(f'O IMC é {imc:.2f} ==> Obesidade extrema')
        somaob += 1

perc_ma = somama/p*100
perc_ob = somaob/p*100
print(f'Percentual com magreza grave: {perc_ma:.2f}%')
print(f'Percentual com obesidade grave: {perc_ob:.2f}%')
