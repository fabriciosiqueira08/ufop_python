peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura: '))
sexo = str(input('Informe seu sexo: '))
imc = peso/(altura**2)


if sexo == 'M':
       
    if imc <=25:
         print(f'Seu IMC é: {imc:.2f}')
         print('Seu IMC está de acordo com a referência.')
    else:
        print(f'Seu IMC é: {imc:.2f}')
        print('Seu IMC está acima da referência.')
else:
    if imc <= 24:
        print(f'Seu IMC é: {imc:.2f}')
        print('Seu IMC está de acordo com a referência.')
    else:
        print(f'Seu IMC é: {imc:.2f}')
        print('Seu IMC está acima da referência.')